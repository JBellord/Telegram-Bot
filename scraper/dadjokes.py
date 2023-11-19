import requests, os

API_NINJA_KEY="EQBCJsucp7M90RXpLcDbkQ==60lesYsM7kI5sqPV"
url = "https://api.api-ninjas.com/v1/dadjokes?limit=1"

def get_dad_jokes():
    res = requests.get(url, headers={'X-Api-Key': API_NINJA_KEY})
    if res.status_code == 200:
        res = res.json()
        return res[0]["joke"]

get_dad_jokes()