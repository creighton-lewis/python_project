import requests
import os
target = input("Enter company name: ")
print (target)

response = os.system(f"curl --request GET \
     --url 'https://api.apollo.io/api/v1/organizations/enrich?domain=target.com' \
     --header 'Cache-Control: no-cache' \
     --header 'Content-Type: application/json' \
     --header 'accept: application/json' \
     --header 'x-api-key: API_KEY'")
print (response)