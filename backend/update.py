import requests
import datetime
import json

tupleCount = (2, 10, 18, 21, 25)

sunday = {
    {'8:00a': None}, {'8:30a': None}, {'9:00a': None}, {'9:30a': None}, {'10:00a': None}, {'10:30a': None},
    {'11:00a': None}, {'11:30a': None}, {'12:00': None}, {'12:30': None}, {'1:00': None}, {'1:30': None},
    {'2:00': None}, {'2:30': None}, {'3:00': None}, {'3:30': None}, {'4:00': None}, {'4:30': None}, {'5:00': None},
    {'5:30': None}, {'6:00': None}, {'6:30': None}, {'7:00': None}, {'7:30': None}, {'8:00': None}, {'8:30': None},
    {'9:00': None}, {'9:30': None}, {'10:00': None}, {'10:30': None}, {'11:00': None}, {'11:30': None}
}

mon_thurs = {
    {'6:00a': None}, {'6:30a': None}, {'7:00a': None}, {'7:30a': None}, {'8:00a': None}, {'8:30a': None},
    {'9:00a': None}, {'9:30a': None}, {'10:00a': None}, {'10:30a': None}, {'11:00a': None}, {'11:30a': None},
    {'12:00': None}, {'12:30': None}, {'1:00': None}, {'1:30': None}, {'2:00': None}, {'2:30': None}, {'3:00': None},
    {'3:30': None}, {'4:00': None}, {'4:30': None}, {'5:00': None}, {'5:30': None}, {'6:00': None}, {'6:30': None},
    {'7:00': None}, {'7:30': None}, {'8:00': None}, {'8:30': None}, {'9:00': None}, {'9:30': None}, {'10:00': None},
    {'10:30': None}, {'11:00': None}, {'11:30': None}
}

friday = {
    {'6:00a': None}, {'6:30a': None}, {'7:00a': None}, {'7:30a': None}, {'8:00a': None}, {'8:30a': None},
    {'9:00a': None}, {'9:30a': None}, {'10:00a': None}, {'10:30a': None}, {'11:00a': None}, {'11:30a': None},
    {'12:00': None}, {'12:30': None}, {'1:00': None}, {'1:30': None}, {'2:00': None}, {'2:30': None}, {'3:00': None},
    {'3:30': None}, {'4:00': None}, {'4:30': None}, {'5:00': None}, {'5:30': None}, {'6:00': None}, {'6:30': None},
    {'7:00': None}, {'7:30': None}, {'8:00': None}, {'8:30': None}, {'9:00': None}, {'9:30': None}
}

saturday = {
    {'8:00a': None}, {'8:30a': None}, {'9:00a': None}, {'9:30a': None}, {'10:00a': None}, {'10:30a': None},
    {'11:00a': None}, {'11:30a': None}, {'12:00': None}, {'12:30': None}, {'1:00': None}, {'1:30': None},
    {'2:00': None}, {'2:30': None}, {'3:00': None}, {'3:30': None}, {'4:00': None}, {'4:30': None}, {'5:00': None},
    {'5:30': None}, {'6:00': None}, {'6:30': None}, {'7:00': None}, {'7:30': None}, {'8:00': None}, {'8:30': None},
    {'9:00': None}, {'9:30': None}
}

track_week = {'Sunday': sunday, 'Monday': mon_thurs, 'Tuesday': mon_thurs, 'Wednesday': mon_thurs,
              'Thursday': mon_thurs, 'Friday': friday, 'Saturday': saturday}

level1_week = {'Sunday': sunday, 'Monday': mon_thurs, 'Tuesday': mon_thurs, 'Wednesday': mon_thurs,
               'Thursday': mon_thurs, 'Friday': friday, 'Saturday': saturday}

level2_week = {'Sunday': sunday, 'Monday': mon_thurs, 'Tuesday': mon_thurs, 'Wednesday': mon_thurs,
               'Thursday': mon_thurs, 'Friday': friday, 'Saturday': saturday}

level3_week = {'Sunday': sunday, 'Monday': mon_thurs, 'Tuesday': mon_thurs, 'Wednesday': mon_thurs,
               'Thursday': mon_thurs, 'Friday': friday, 'Saturday': saturday}

power_week = {'Sunday': sunday, 'Monday': mon_thurs, 'Tuesday': mon_thurs, 'Wednesday': mon_thurs,
              'Thursday': mon_thurs, 'Friday': friday, 'Saturday': saturday}


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
