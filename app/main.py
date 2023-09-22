from datetime import date, timedelta
from team_utilities import match_extraction, except_messgs
from ref_utilities import refreehist_extraction, refexcept_messgs
from var import testleagues_list


def main():
    today = date.today()
    tomorrow = date.today() + timedelta(days=1)
    print(today, tomorrow)

    match_extraction(testleagues_list, tomorrow)
    refreehist_extraction(testleagues_list, tomorrow)
    for key in except_messgs.keys():
        print(f"{key}: {except_messgs[key]}")
    for key in refexcept_messgs.keys():
        print(f"{key}: {refexcept_messgs[key]}")


if __name__ == '__main__':
    main()