import requests
import datetime
import json

tupleCount = (2, 10, 18, 21, 25)


class sunday:
    def __init__(self):
        self.times = [{'08:00': None, 'count': 0}, {'08:30': None, 'count': 0}, {'09:00': None, 'count': 0},
                      {'09:30': None, 'count': 0}, {'10:00': None, 'count': 0}, {'10:30': None, 'count': 0},
                      {'11:00': None, 'count': 0}, {'11:30': None, 'count': 0}, {'12:00': None, 'count': 0},
                      {'12:30': None, 'count': 0}, {'13:00': None, 'count': 0}, {'13:30': None, 'count': 0},
                      {'14:00': None, 'count': 0}, {'14:30': None, 'count': 0}, {'15:00': None, 'count': 0},
                      {'15:30': None, 'count': 0}, {'16:00': None, 'count': 0}, {'16:30': None, 'count': 0},
                      {'17:00': None, 'count': 0}, {'17:30': None, 'count': 0}, {'18:00': None, 'count': 0},
                      {'18:30': None, 'count': 0}, {'19:00': None, 'count': 0}, {'19:30': None, 'count': 0},
                      {'20:00': None, 'count': 0}, {'20:30': None, 'count': 0}, {'21:00': None, 'count': 0},
                      {'21:30': None, 'count': 0}, {'22:00': None, 'count': 0}, {'22:30': None, 'count': 0},
                      {'23:00': None, 'count': 0}, {'23:30': None, 'count': 0}]


class mon_thurs:
    def __init__(self):
        self.times = [{'06:00': None, 'count': 0}, {'06:30': None, 'count': 0}, {'07:00': None, 'count': 0},
                      {'07:30': None, 'count': 0}, {'08:00': None, 'count': 0}, {'08:30': None, 'count': 0},
                      {'09:00': None, 'count': 0}, {'09:30': None, 'count': 0}, {'10:00': None, 'count': 0},
                      {'10:30': None, 'count': 0}, {'11:00': None, 'count': 0}, {'11:30': None, 'count': 0},
                      {'12:00': None, 'count': 0}, {'12:30': None, 'count': 0}, {'13:00': None, 'count': 0},
                      {'13:30': None, 'count': 0}, {'14:00': None, 'count': 0}, {'14:30': None, 'count': 0},
                      {'15:00': None, 'count': 0}, {'15:30': None, 'count': 0}, {'16:00': None, 'count': 0},
                      {'16:30': None, 'count': 0}, {'17:00': None, 'count': 0}, {'17:30': None, 'count': 0},
                      {'18:00': None, 'count': 0}, {'18:30': None, 'count': 0}, {'18:00': None, 'count': 0},
                      {'19:30': None, 'count': 0}, {'20:00': None, 'count': 0}, {'20:30': None, 'count': 0},
                      {'21:00': None, 'count': 0}, {'21:30': None, 'count': 0}, {'22:00': None, 'count': 0},
                      {'22:30': None, 'count': 0}, {'23:00': None, 'count': 0}, {'23:30': None, 'count': 0}]


class friday:
    def __init__(self):
        self.times = [{'06:00': None, 'count': 0}, {'06:30': None, 'count': 0}, {'07:00': None, 'count': 0},
                      {'07:30': None, 'count': 0}, {'08:00': None, 'count': 0}, {'08:30': None, 'count': 0},
                      {'09:00': None, 'count': 0}, {'09:30': None, 'count': 0}, {'10:00': None, 'count': 0},
                      {'10:30': None, 'count': 0}, {'11:00': None, 'count': 0}, {'11:30': None, 'count': 0},
                      {'12:00': None, 'count': 0}, {'12:30': None, 'count': 0}, {'13:00': None, 'count': 0},
                      {'13:30': None, 'count': 0}, {'14:00': None, 'count': 0}, {'14:30': None, 'count': 0},
                      {'15:00': None, 'count': 0}, {'15:30': None, 'count': 0}, {'16:00': None, 'count': 0},
                      {'16:30': None, 'count': 0}, {'17:00': None, 'count': 0}, {'17:30': None, 'count': 0},
                      {'18:00': None, 'count': 0}, {'18:30': None, 'count': 0}, {'19:00': None, 'count': 0},
                      {'19:30': None, 'count': 0}, {'20:00': None, 'count': 0}, {'20:30': None, 'count': 0},
                      {'21:00': None, 'count': 0}, {'21:30': None, 'count': 0}]


class saturday:
    def __init__(self):
        self.times = [{'08:00': None, 'count': 0}, {'08:30': None, 'count': 0}, {'09:00': None, 'count': 0},
                      {'09:30': None, 'count': 0}, {'10:00': None, 'count': 0}, {'10:30': None, 'count': 0},
                      {'11:00': None, 'count': 0}, {'11:30': None, 'count': 0}, {'12:00': None, 'count': 0},
                      {'12:30': None, 'count': 0}, {'13:00': None, 'count': 0}, {'13:30': None, 'count': 0},
                      {'14:00': None, 'count': 0}, {'14:30': None, 'count': 0}, {'15:00': None, 'count': 0},
                      {'15:30': None, 'count': 0}, {'16:00': None, 'count': 0}, {'16:30': None, 'count': 0},
                      {'17:00': None, 'count': 0}, {'17:30': None, 'count': 0}, {'18:00': None, 'count': 0},
                      {'18:30': None, 'count': 0}, {'19:00': None, 'count': 0}, {'19:30': None, 'count': 0},
                      {'20:00': None, 'count': 0}, {'20:30': None, 'count': 0}, {'21:00': None, 'count': 0},
                      {'21:30': None, 'count': 0}]


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

def get_date(parsed_json):
    track = datetime.date(int(parsed_json[0]["LastUpdatedDateAndTime"][0:4]), int(parsed_json[0]["LastUpdatedDateAndTime"][5:7]),
     int(parsed_json[0]["LastUpdatedDateAndTime"][8:10]))

    level3 = datetime.date(int(parsed_json[1]["LastUpdatedDateAndTime"][0:4]), int(parsed_json[1]["LastUpdatedDateAndTime"][5:7]),
     int(parsed_json[1]["LastUpdatedDateAndTime"][8:10]))

    level2 = datetime.date(int(parsed_json[2]["LastUpdatedDateAndTime"][0:4]), int(parsed_json[2]["LastUpdatedDateAndTime"][5:7]),
     int(parsed_json[2]["LastUpdatedDateAndTime"][8:10]))

    level1 = datetime.date(int(parsed_json[3]["LastUpdatedDateAndTime"][0:4]), int(parsed_json[3]["LastUpdatedDateAndTime"][5:7]),
     int(parsed_json[3]["LastUpdatedDateAndTime"][8:10]))

    powerHouse = datetime.date(int(parsed_json[4]["LastUpdatedDateAndTime"][0:4]), int(parsed_json[4]["LastUpdatedDateAndTime"][5:7]),
     int(parsed_json[4]["LastUpdatedDateAndTime"][8:10]))

    return track, level3, level2, level1, powerHouse

def get_time(parsed_json):
    track = parsed_json[0]["LastUpdatedDateAndTime"][parsed_json[0]["LastUpdatedDateAndTime"].
    index('T') + 1:parsed_json[0]["LastUpdatedDateAndTime"].index('.')]

    if int(track[3:5]) > 30: # rounds down to nearest half hour
        track = track[0:3] + "30"
    else:
        track = track[0:3] + "00" 

    level3 = parsed_json[1]["LastUpdatedDateAndTime"][parsed_json[1]["LastUpdatedDateAndTime"].
    index('T') + 1:parsed_json[1]["LastUpdatedDateAndTime"].index('.')]

    if int(level3[3:5]) > 30: # rounds down to nearest half hour
        level3 = level3[0:3] + "30"
    else:
        level3 = level3[0:3] + "00" 

    level2 = parsed_json[2]["LastUpdatedDateAndTime"][parsed_json[2]["LastUpdatedDateAndTime"].
    index('T') + 1:parsed_json[2]["LastUpdatedDateAndTime"].index('.')]

    if int(level2[3:5]) > 30: # rounds down to nearest half hour
        level2 = level2[0:3] + "30"
    else:
        level2 = level2[0:3] + "00" 

    level1 = parsed_json[3]["LastUpdatedDateAndTime"][parsed_json[3]["LastUpdatedDateAndTime"].
    index('T') + 1:parsed_json[3]["LastUpdatedDateAndTime"].index('.')]

    if int(level1[3:5]) > 30: # rounds down to nearest half hour
        level1 = level1[0:3] + "30"
    else:
        level1 = level1[0:3] + "00" 

    powerHouse = parsed_json[4]["LastUpdatedDateAndTime"][parsed_json[4]["LastUpdatedDateAndTime"].
    index('T') + 1:parsed_json[4]["LastUpdatedDateAndTime"].index('.')]

    if int(powerHouse[3:5]) > 30: # rounds down to nearest half hour
        powerHouse = powerHouse[0:3] + "30"
    else:
        powerHouse = powerHouse[0:3] + "00" 

    return track, level3, level2, level1, powerHouse

def get_day(trackDate, lvl3Date, lvl2Date, lvl1Date, phDate):
    days = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

    return days[trackDate.weekday()], days[lvl3Date.weekday()], days[lvl2Date.weekday()], days[lvl1Date.weekday()], days[phDate.weekday()]

def update_structure():
    parsed_json = api_to_json()

    

    trackTime, lvl3Time, lvl2Time, lvl1Time, phTime = get_time(parsed_json)
    trackDate, lvl3Date, lvl2Date, lvl1Date, phDate = get_date(parsed_json)
    trackDay, lvl3Day, lvl2Day, lvl1Day, phDay = get_day(trackDate, lvl3Date, lvl2Date, lvl1Date, phDate)
    return trackDay, lvl3Day, lvl2Day, lvl1Day, phDay
