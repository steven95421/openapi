import requests
params = {"email": "v-syang@microsoft.com", "key": "silverhawk25"

          }


url = "https://aqs.epa.gov/data/api/list/states"
response = requests.get(url, params=params)
print(response.json())