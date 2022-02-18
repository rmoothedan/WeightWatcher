import requests


def get_api():
    payload = {'key1': 'value'}
    r = requests.get('https://goboardapi.azurewebsites.net/api/FacilityCount/GetCountsByAccount?AccountAPIKey'
                     '=7938FC89-A15C-492D-9566-12C961BC1F27', params=payload)
    return r.text
