import requests
import json

key = ""
host = "apidojo-yahoo-finance-v1.p.rapidapi.com"

def get_history(ticker):
    
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-historical-data"

    querystring = {"symbol":ticker,"region":"US"}
    
    headers = {
        'x-rapidapi-key': key,
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    
    return response.json()

