import requests
import datetime
import json

tupleCount = (2, 10, 18, 21, 25)
dictOfWeek = {'Sunday': [], 'Monday': [], 'Tuesday': [], 'Wednesday': [],
              'Thursday': [], 'Friday': [], 'Saturday': []}


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
    pass
