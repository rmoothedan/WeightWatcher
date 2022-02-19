import requests
import json


# todo figure out data structures to hold parsed JSON
# todo figure out how to best access fields
# mooth branch
def get_api():
    payload = {'AccountAPIKey': '7938FC89-A15C-492D-9566-12C961BC1F27'}
    r = requests.get('https://goboardapi.azurewebsites.net/api/FacilityCount/GetCountsByAccount', params=payload)
    return r


def api_to_json():
    apiCall = get_api()
    apiCall = apiCall.json()
    apiParsed = parse_json(apiCall)
    return apiParsed


def parse_json(json_list):
    json_list
    return json_list
