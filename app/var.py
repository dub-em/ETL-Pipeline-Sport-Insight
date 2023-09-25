#Dictionary containing the urls of each league for the different sites extracted from.

leagues_list = {
    'English Premier League':['https://www.flashscore.nl/voetbal/engeland/premier-league/schema/', 'https://www.worldfootball.net/all_matches/eng-premier-league-2023-2024/'],
    'Championship':['https://www.flashscore.nl/voetbal/engeland/championship/schema/','https://www.worldfootball.net/all_matches/eng-championship-2023-2024/'],
    'EFL Championship':['https://www.flashscore.nl/voetbal/engeland/efl-cup/schema/', ''],
    'EFL Trophy':['https://www.flashscore.nl/voetbal/engeland/efl-trophy/schema/', 'https://www.worldfootball.net/all_matches/eng-efl-trophy-2023-2024/'],
    'La Liga':['https://www.flashscore.nl/voetbal/spanje/laliga/schema/','https://www.worldfootball.net/all_matches/esp-primera-division-2023-2024/'],
    'La Liga2':['https://www.flashscore.nl/voetbal/spanje/laliga2/schema/', 'https://www.worldfootball.net/all_matches/esp-segunda-division-2023-2024/'],
    'Bundesliga':['https://www.flashscore.nl/voetbal/duitsland/bundesliga/schema/', 'https://www.worldfootball.net/all_matches/bundesliga-2023-2024/'],
    'Serie A':['https://www.flashscore.nl/voetbal/italie/serie-a/schema/', 'https://www.worldfootball.net/all_matches/ita-serie-a-2023-2024/'],
    'Serie B':['https://www.flashscore.nl/voetbal/italie/serie-b/schema/', 'https://www.worldfootball.net/all_matches/ita-serie-b-2023-2024/'],
    'Ligue 1':['https://www.flashscore.nl/voetbal/frankrijk/ligue-1/schema/', 'https://www.worldfootball.net/all_matches/fra-ligue-1-2023-2024/'],
    'Ligue 2':['https://www.flashscore.nl/voetbal/frankrijk/ligue-2/schema/', 'https://www.worldfootball.net/all_matches/fra-ligue-2-2023-2024/'],
    'Brasileirão Serie A':['https://www.flashscore.nl/voetbal/brazilie/braziliaanse-competitie/schema/', 'https://www.worldfootball.net/all_matches/bra-serie-a-2023/'],
    'Primera División':['https://www.flashscore.nl/voetbal/argentinie/primera-d/schema/', ''],
    'Major League Soccer':['https://www.flashscore.nl/voetbal/usa/mls/schema/', 'https://www.worldfootball.net/all_matches/usa-major-league-soccer-2023/'],
    'Eredivisie':['https://www.flashscore.nl/eredivisie/schema/', 'https://www.worldfootball.net/all_matches/ned-eredivisie-2023-2024/'],
    'Primeira Liga':['https://www.flashscore.nl/voetbal/portugal/liga-portugal/schema/', 'https://www.worldfootball.net/all_matches/por-primeira-liga-2023-2024/'],
    'J1 League':['https://www.flashscore.nl/voetbal/japan/j1-league/schema/', 'https://www.worldfootball.net/all_matches/jpn-j1-league-2023/'],
    'Scottish Premiership':['https://www.flashscore.nl/voetbal/schotland/premiership/schema/', 'https://www.worldfootball.net/all_matches/sco-premiership-2023-2024/'],
    'Superliga':['https://www.flashscore.nl/voetbal/denemarken/superliga/schema/', 'https://www.worldfootball.net/all_matches/den-superligaen-2023-2024/'],
    'Süper Lig':['https://www.flashscore.nl/voetbal/turkije/super-lig/schema/', 'https://www.worldfootball.net/all_matches/tur-sueperlig-2023-2024/'],
    'Allsvenskan':['https://www.flashscore.nl/voetbal/zweden/allsvenskan/schema/', 'https://www.worldfootball.net/all_matches/swe-allsvenskan-2023/'],
    'Saudi Professional League':['https://www.flashscore.nl/voetbal/saoedi-arabie/premier-league/schema/', 'https://www.worldfootball.net/all_matches/ksa-saudi-pro-league-2023-2024/'],
    'Jupiler Pro League':['https://www.flashscore.nl/voetbal/belgie/jupiler-pro-league/schema/', 'https://www.worldfootball.net/all_matches/bel-eerste-klasse-a-2023-2024/'],
    'UEFA Champions League':['https://www.flashscore.nl/voetbal/europa/champions-league/schema/', 'https://www.worldfootball.net/all_matches/champions-league-2023-2024/'],
    'UEFA Europa League':['https://www.flashscore.nl/voetbal/europa/europa-league/schema/', 'https://www.worldfootball.net/all_matches/europa-league-2023-2024/'],
    'UEFA Europa Conference League':['https://www.flashscore.nl/voetbal/europa/europa-conference-league/schema/', 'https://www.worldfootball.net/all_matches/europa-conference-league-2023-2024/'],
}


testleagues_list = {
    #'English Premier League':['https://www.flashscore.nl/voetbal/engeland/premier-league/schema/', 'https://www.worldfootball.net/all_matches/eng-premier-league-2023-2024/'],
    #'EFL Championship':['https://www.flashscore.nl/voetbal/engeland/efl-cup/schema/', ''],
    #'EFL Trophy':['https://www.flashscore.nl/voetbal/engeland/efl-trophy/schema/', 'https://www.worldfootball.net/all_matches/eng-efl-trophy-2023-2024/'],
    #'Ligue 1':['https://www.flashscore.nl/voetbal/frankrijk/ligue-1/schema/', 'https://www.worldfootball.net/all_matches/fra-ligue-1-2023-2024/'],
    'La Liga':['https://www.flashscore.nl/voetbal/spanje/laliga/schema/','https://www.worldfootball.net/all_matches/esp-primera-division-2023-2024/'],
    'La Liga2':['https://www.flashscore.nl/voetbal/spanje/laliga2/schema/', 'https://www.worldfootball.net/all_matches/esp-segunda-division-2023-2024/'],
    'Serie A':['https://www.flashscore.nl/voetbal/italie/serie-a/schema/', 'https://www.worldfootball.net/all_matches/ita-serie-a-2023-2024/'],
    'Serie B':['https://www.flashscore.nl/voetbal/italie/serie-b/schema/', 'https://www.worldfootball.net/all_matches/ita-serie-b-2023-2024/'],
    #'Major League Soccer':['https://www.flashscore.nl/voetbal/usa/mls/schema/', 'https://www.worldfootball.net/all_matches/usa-major-league-soccer-2023/'],
    #'Bundesliga':['https://www.flashscore.nl/voetbal/duitsland/bundesliga/schema/', 'https://www.worldfootball.net/all_matches/bundesliga-2023-2024/'], 
}


exe_path = r'C:/Users/hp/Documents/Our Documents/Personal Development/Projects/Client Projects/Dexter Hadeveld (Upwork)/ETL-Pipeline-Sport-Insight/app/chromedriver-win64/chromedriver.exe'