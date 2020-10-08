import requests

params = {
    "email": "v-syang@microsoft.com",
    "key": "silverhawk25",
}

url = "https://aqs.epa.gov/data/api/list/classes"
response = requests.get(url, params=params)
# print(response.json())

params['pc'] = "AQI POLLUTANTS"

url = "https://aqs.epa.gov/data/api/list/parametersByClass"
response = requests.get(url, params=params)
print(response.json())
params = {
    "email": "v-syang@microsoft.com",
    "key": "silverhawk25",
    "param": "42602",
    "bdate": "200925",
    "edate": "20201006",
    "state": "37"
}
url = "https://aqs.epa.gov/data/api/dailyData/byState"
response = requests.get(url, params=params)
print(response.json())
