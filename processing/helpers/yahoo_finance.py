import requests
import json

def get_history(ticker):
    
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-historical-data"

    querystring = {"symbol":ticker,"region":"US"}
    
    headers = {
        'x-rapidapi-key': "d382e352ccmsh3171df9b4c2bf33p104bddjsn4d0e0591aabc",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    
    return response.json()

