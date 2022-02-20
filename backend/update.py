import requests
import datetime
import json

tupleCount = (2, 10, 18, 21, 25)


class sunday:
    def __init__(self):
        self.times = {{'8:00a': None, 'count': 0}, {'8:30a': None, 'count': 0}, {'9:00a': None, 'count': 0},
                      {'9:30a': None, 'count': 0}, {'10:00a': None, 'count': 0}, {'10:30a': None, 'count': 0},
                      {'11:00a': None, 'count': 0}, {'11:30a': None, 'count': 0}, {'12:00': None, 'count': 0},
                      {'12:30': None, 'count': 0}, {'1:00': None, 'count': 0}, {'1:30': None, 'count': 0},
                      {'2:00': None, 'count': 0}, {'2:30': None, 'count': 0}, {'3:00': None, 'count': 0},
                      {'3:30': None, 'count': 0}, {'4:00': None, 'count': 0}, {'4:30': None, 'count': 0},
                      {'5:00': None, 'count': 0}, {'5:30': None, 'count': 0}, {'6:00': None, 'count': 0},
                      {'6:30': None, 'count': 0}, {'7:00': None, 'count': 0}, {'7:30': None, 'count': 0},
                      {'8:00': None, 'count': 0}, {'8:30': None, 'count': 0}, {'9:00': None, 'count': 0},
                      {'9:30': None, 'count': 0}, {'10:00': None, 'count': 0}, {'10:30': None, 'count': 0},
                      {'11:00': None, 'count': 0}, {'11:30': None, 'count': 0}}


class mon_thurs:
    def __init__(self):
        self.times = {{'6:00a': None, 'count': 0}, {'6:30a': None, 'count': 0}, {'7:00a': None, 'count': 0},
                      {'7:30a': None, 'count': 0}, {'8:00a': None, 'count': 0}, {'8:30a': None, 'count': 0},
                      {'9:00a': None, 'count': 0}, {'9:30a': None, 'count': 0}, {'10:00a': None, 'count': 0},
                      {'10:30a': None, 'count': 0}, {'11:00a': None, 'count': 0}, {'11:30a': None, 'count': 0},
                      {'12:00': None, 'count': 0}, {'12:30': None, 'count': 0}, {'1:00': None, 'count': 0},
                      {'1:30': None, 'count': 0}, {'2:00': None, 'count': 0}, {'2:30': None, 'count': 0},
                      {'3:00': None, 'count': 0}, {'3:30': None, 'count': 0}, {'4:00': None, 'count': 0},
                      {'4:30': None, 'count': 0}, {'5:00': None, 'count': 0}, {'5:30': None, 'count': 0},
                      {'6:00': None, 'count': 0}, {'6:30': None, 'count': 0}, {'7:00': None, 'count': 0},
                      {'7:30': None, 'count': 0}, {'8:00': None, 'count': 0}, {'8:30': None, 'count': 0},
                      {'9:00': None, 'count': 0}, {'9:30': None, 'count': 0}, {'10:00': None, 'count': 0},
                      {'10:30': None, 'count': 0}, {'11:00': None, 'count': 0}, {'11:30': None, 'count': 0}}


class friday:
    def __init__(self):
        self.times = {{'6:00a': None, 'count': 0}, {'6:30a': None, 'count': 0}, {'7:00a': None, 'count': 0},
                      {'7:30a': None, 'count': 0}, {'8:00a': None, 'count': 0}, {'8:30a': None, 'count': 0},
                      {'9:00a': None, 'count': 0}, {'9:30a': None, 'count': 0}, {'10:00a': None, 'count': 0},
                      {'10:30a': None, 'count': 0}, {'11:00a': None, 'count': 0}, {'11:30a': None, 'count': 0},
                      {'12:00': None, 'count': 0}, {'12:30': None, 'count': 0}, {'1:00': None, 'count': 0},
                      {'1:30': None, 'count': 0}, {'2:00': None, 'count': 0}, {'2:30': None, 'count': 0},
                      {'3:00': None, 'count': 0}, {'3:30': None, 'count': 0}, {'4:00': None, 'count': 0},
                      {'4:30': None, 'count': 0}, {'5:00': None, 'count': 0}, {'5:30': None, 'count': 0},
                      {'6:00': None, 'count': 0}, {'6:30': None, 'count': 0}, {'7:00': None, 'count': 0},
                      {'7:30': None, 'count': 0}, {'8:00': None, 'count': 0}, {'8:30': None, 'count': 0},
                      {'9:00': None, 'count': 0}, {'9:30': None, 'count': 0}}


class saturday:
    def __init__(self):
        self.times = {{'8:00a': None, 'count': 0}, {'8:30a': None, 'count': 0}, {'9:00a': None, 'count': 0},
                      {'9:30a': None, 'count': 0}, {'10:00a': None, 'count': 0}, {'10:30a': None, 'count': 0},
                      {'11:00a': None, 'count': 0}, {'11:30a': None, 'count': 0}, {'12:00': None, 'count': 0},
                      {'12:30': None, 'count': 0}, {'1:00': None, 'count': 0}, {'1:30': None, 'count': 0},
                      {'2:00': None, 'count': 0}, {'2:30': None, 'count': 0}, {'3:00': None, 'count': 0},
                      {'3:30': None, 'count': 0}, {'4:00': None, 'count': 0}, {'4:30': None, 'count': 0},
                      {'5:00': None, 'count': 0}, {'5:30': None, 'count': 0}, {'6:00': None, 'count': 0},
                      {'6:30': None, 'count': 0}, {'7:00': None, 'count': 0}, {'7:30': None, 'count': 0},
                      {'8:00': None, 'count': 0}, {'8:30': None, 'count': 0}, {'9:00': None, 'count': 0},
                      {'9:30': None, 'count': 0}}


trackSun = sunday()
trackMon = mon_thurs()
trackTues = mon_thurs()
trackWed = mon_thurs()
trackThurs = mon_thurs()
trackFri = friday()
trackSat = saturday()
track_week = {'Sunday': trackSun, 'Monday': trackMon, 'Tuesday': trackTues, 'Wednesday': trackWed,
              'Thursday': trackThurs, 'Friday': trackFri, 'Saturday': trackSat}


lvl1Sun = sunday()
lvl1Mon = mon_thurs()
lvl1Tues = mon_thurs()
lvl1Wed = mon_thurs()
lvl1Thurs = mon_thurs()
lvl1Fri = friday()
lvl1Sat = saturday()
level1_week = {'Sunday': lvl1Sun, 'Monday': lvl1Mon, 'Tuesday': lvl1Tues, 'Wednesday': lvl1Wed,
               'Thursday': lvl1Thurs, 'Friday': lvl1Fri, 'Saturday': lvl1Sat}

lvl2Sun = sunday()
lvl2Mon = mon_thurs()
lvl2Tues = mon_thurs()
lvl2Wed = mon_thurs()
lvl2Thurs = mon_thurs()
lvl2Fri = friday()
lvl2Sat = saturday()
level2_week = {'Sunday': lvl2Sun, 'Monday': lvl2Mon, 'Tuesday': lvl2Tues, 'Wednesday': lvl2Wed,
               'Thursday': lvl2Thurs, 'Friday': lvl2Fri, 'Saturday': lvl2Sat}

lvl3Sun = sunday()
lvl3Mon = mon_thurs()
lvl3Tues = mon_thurs()
lvl3Wed = mon_thurs()
lvl3Thurs = mon_thurs()
lvl3Fri = friday()
lvl3Sat = saturday()
level3_week = {'Sunday': lvl3Sun, 'Monday': lvl3Mon, 'Tuesday': lvl3Tues, 'Wednesday': lvl3Wed,
               'Thursday': lvl3Thurs, 'Friday': lvl3Fri, 'Saturday': lvl3Sat}

powerSun = sunday()
powerMon = mon_thurs()
powerTues = mon_thurs()
powerWed = mon_thurs()
powerThurs = mon_thurs()
powerFri = friday()
powerSat = saturday()
power_week = {'Sunday': powerSun, 'Monday': powerMon, 'Tuesday': powerTues, 'Wednesday': powerWed,
              'Thursday': powerThurs, 'Friday': powerFri, 'Saturday': powerSat}


def get_api():
    payload = {'AccountAPIKey': '7938FC89-A15C-492D-9566-12C961BC1F27'}
    r = requests.get('https://goboardapi.azurewebsites.net/api/FacilityCount/GetCountsByAccount', params=payload)
    return r


def api_to_json():
    apiCall = get_api().text
    json_dict = json.loads(apiCall)
    apiParsed = parse_json(json_dict)
    return apiParsed


def parse_json(json_dict):
    parsed = []
    for i in range(5):
        parsed.append(json_dict[tupleCount[i]])
    return parsed


def update_structure(parsed_json):
    # todo
    # for each JSON member
        # if DateTime = correct
            # update today: (prev avg + new val) / (n+1)
    pass
