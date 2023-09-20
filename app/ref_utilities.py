from bs4 import BeautifulSoup
import time, os, psycopg2, json, requests
import pandas as pd
import numpy as np
from config import settings

refexcept_messgs = {}

def refdata_loader(dataset):
    #Extracting the data from the dataframe to load into the database multiple rows at a time
    lim = dataset.shape[0]

    ref_data = []
    for i in range(lim):
        ref_data.append(dataset.iloc[i,:])

    #PostgreSQL database connection parameters
    connection_params = {
        "host": settings.host,
        "port": settings.port,
        "database": settings.database,
        "user": settings.user,
        "password": settings.password
    }

    #Connect to PostgreSQL
    connection = psycopg2.connect(**connection_params)
    cursor = connection.cursor()

    create_query = '''CREATE TABLE IF NOT EXISTS ref_historic_match (
        date VARCHAR,
        time VARCHAR,
        hometeam VARCHAR,
        awayteam VARCHAR,
        result VARCHAR,
        matchlink VARCHAR,
        league VARCHAR,
        refereelink VARCHAR,
        referee_matchistlink JSONB,
        referee_matchhistdetails JSONB
    );'''
    cursor.execute(create_query)

    #Insert all the data into the table multiple rows at a time
    insert_query = "INSERT INTO ref_historic_match (date, time, hometeam, awayteam, result, matchlink, league, refereelink, referee_matchistlink, referee_matchhistdetails) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    cursor.executemany(insert_query, ref_data)

    #Commit and close connection
    connection.commit()
    cursor.close()
    connection.close()


def refreehist_extraction(leagues_list, today_date):
    leagues_dataset = {} #Created the empyt dictionary that will be used to concatenate all table from all leagues

    for key in list(leagues_list.keys()): #Loops through all the leagues in our list of league url
        league_url = leagues_list[key][1]

        league_counter = 0
        try:
            if league_url == '': 
                #Checks for empty league links and skips
                continue
            else:
                #Gets the contents from the leagues schedule page
                response = requests.get(league_url)
                time.sleep(2)
                soup = BeautifulSoup(response.content, "html.parser")

                #Extracts the table with the match schedules
                table = soup.find("table", class_="standard_tabelle")

                data = []
                match_links = []

                #Extracts the table rows
                table_rows = table.find_all("tr")
                for row in table_rows:
                    #Loops through al the rows and extracts the data in each columns
                    columns = row.find_all("td")
                    row_data = [column.get_text(strip=True) for column in columns]
                    data.append(row_data)

                    #Extracts the urls of each match
                    match_link = row.find("a", href=lambda href: href and "report" in href)
                    if match_link:
                        match_links.append(match_link["href"])
                    else:
                        match_links.append('')

                #Drops the empty entries
                zipped_lists = zip(data, match_links)
                zipped_lists = [pair for pair in zipped_lists if len(pair[0]) > 0]
                data, match_links = zip(*zipped_lists)

                columns = ['Date', 'Time', 'Home Team', 'Score', 'Away Team', 'Result', 'Links']
                df = pd.DataFrame(data, columns=columns)
                df.Links = match_links

                df = df[df['Links'] != ''] #Drops columns with empty url

                #Add the prefix to the column
                df['Links'] = 'https://www.worldfootball.net' + df['Links']
                df['Date'] = df['Date'].replace('', np.nan).ffill()
                df['Date'] = pd.to_datetime(df['Date'],  format='%d/%m/%Y')

                #Filter rows with today's date
                today_df = df[df['Date'].dt.date == today_date] #Account for when the dataset filter everything due to no matching date
                today_df = today_df.copy(deep=True)
                curr_league = [key for i in range(len(today_df['Links']))]
                today_df['League'] = curr_league

                #Extracts the link to the profile of the officiating referee from the match page using match url
                referee_urls = []
                for match_url in today_df.Links:
                    response = requests.get(match_url)
                    html_content = response.content
                    soup = BeautifulSoup(html_content, "html.parser")
                    referee_links = soup.find_all("a", href=lambda href: href and "referee_summary" in href)
                    ref_link = []
                    if len(referee_links) > 0:
                        for link in referee_links:
                            link_url = link.get("href")
                            ref_link.append(f'https://www.worldfootball.net{link_url}')
                            
                        ref_link = ref_link[0]
                        referee_urls.append(ref_link)
                    else:
                        referee_urls.append('')

                #Add the url of the profile of the officiating referee of each match to dataframe containing daily matches
                today_df['Referee_Links'] = referee_urls

                #Extracts the url of the most recent matches officiated by the officiating referee
                ref_matchhist_url = []
                for ref_url in today_df.Referee_Links:
                    if ref_url != '':
                        ref_matchhist = []

                        response = requests.get(ref_url)
                        html_content = response.content

                        soup = BeautifulSoup(html_content, "html.parser")

                        table = soup.find("table")
                        rows = table.find_all("tr")

                        for row in rows:
                            columns = row.find_all("td")
                            for column in columns:
                                (column.get_text())

                        referee_summary_links = soup.find_all("a", href=lambda href: href and "referee_summary" and "2023-2024" and "2022-2023" in href)

                        for link in referee_summary_links:
                            link_url = link.get("href")
                            ref_matchhist.append(f'https://www.worldfootball.net{link_url}')
                        ref_matchhist = [link for link in ref_matchhist if 'referee_summary' in link]
                        
                        ref_matchhist = {'1':ref_matchhist}
                        ref_matchhist = json.dumps(ref_matchhist)
                        ref_matchhist_url.append(ref_matchhist)
                    else:
                        ref_matchhist_url.append(json.dumps({'1':[]}))

                #Add the urls of the most recent matches officiated by the referee to the dataframe of daily matches
                today_df['Referee_MatchHist_Links'] = ref_matchhist_url

                #Extracts the details from each match and stores in a dictionary
                ref_matchhist_detail = []
                for row in today_df.Referee_MatchHist_Links:
                    transf_row = json.loads(row)
                    if transf_row['1'] != []:
                        data_dict = {'Date':[], 'Home Team':[], 'Away Team':[], 'Score':[], 'Yellow Cards':[], 'Unkown Card':[], 'Red Cards':[]}
                        for ref_match_url in transf_row['1']:
                            response = requests.get(ref_match_url)
                            soup = BeautifulSoup(response.content, "html.parser")

                            table = soup.find("table", class_="standard_tabelle")

                            data = [] # List to store table data

                            table_rows = table.find_all("tr")
                            for row in table_rows:
                                columns = row.find_all("td")
                                row_data = [column.get_text(strip=True) for column in columns]
                                data.append(row_data)

                            data = data[1:]
                            for entry in data:
                                entry.pop(2)

                            for entry in data:
                                for i in range(len(entry)):
                                    keys = list(data_dict.keys())[i]
                                    data_dict[keys].append(entry[i])
                        data_dict = json.dumps(data_dict)
                        ref_matchhist_detail.append(data_dict)
                    else:
                        ref_matchhist_detail.append(json.dumps({}))

                #Extracted match details are added to the dataframe of daily matches
                today_df['Referee_MatchHist_Details'] = ref_matchhist_detail
                today_df.drop('Score', axis=1, inplace=True)
                
                #Loads the extracted league to the database
                for i in range(2): #Tries twice to load data in case of any unforeseen connection issue
                    try:
                        refdata_loader(today_df) #If try is successful, breaks the loop
                        #print("All daily matches of {} have been loaded!".format(key))
                        break
                    except Exception as e:
                        refexcept_messgs[str(key)+f": {league_counter} (Database Loading)"] = f"{type(e).__name__}: {e}" #Catches and Records Error
                        if i < 1: #If try isn't successful but it's the first time, then it tries again
                            continue
                        else: #If try isn't successful the second time, it adds the dataframe to the dictionary to try later.
                            leagues_dataset[key] = today_df
                        league_counter += 1

            #leagues_dataset[key] = today_df #Adds the dataframe of daily matches for a league to the dictionary of leagues
        except Exception as e:
            print('except')
            refexcept_messgs[str(key)+f": {league_counter}"] = f"{type(e).__name__}: {e}" #Catches and Records Error
            league_counter += 1
            continue

    #All the dataframe of the daily matches for all the leagues extracted are concatenated vertically
    list_of_keys = list(leagues_dataset.keys())
    if len(list_of_keys) > 0:
        for i in range(len(list_of_keys)):
            if i == 0:
                key = list_of_keys[i]
                final_dataset = leagues_dataset[key].copy(deep=True)
            else:
                key = list_of_keys[i]
                final_dataset = pd.concat([final_dataset, leagues_dataset[key]], axis=0)

        #Retries to load all the previous data that couldn't be loaded during extraction into the database
        for i in range(2): #Tries twice to load data in case of any unforeseen connection issue
            try:
                refdata_loader(today_df) #If try is successful, breaks the loop
                break
            except Exception as e:
                refexcept_messgs[f"(Final Database Loading): {i} "] = f"{type(e).__name__}: {e}" #Catches and Records Error
                league_counter += 1
                continue #If try isn't successful but it's the first time, then it tries again