import requests 
import urlib.request
import os 
from main import target 

api_key = "a1d14852a2a6d291bede5c402cf0cd8779aa3f5a"
#api_key = input("Enter api key")

try: 
    url = "https://api.hunter.io/v2/companies/find?domain={target}&api_key={a1d14852a2a6d291bede5c402cf0cd8779aa3f5a}}"
    response = print(requests.get(url))
    response.raise_for_status()
    
    # Print the actual data
    data = response.json()
    print(data)
except: 
    print ("Invalid site")
    