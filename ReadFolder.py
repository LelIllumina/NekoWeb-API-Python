import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Use environment variables for sensitive information
API_KEY = os.getenv('NEKOWEB_API_KEY')
url = "https://nekoweb.org/api/files/readfolder"

pathname = input("Path name to query: ")

querystring = {"pathname": pathname}

headers = {"Authorization": API_KEY}

response = requests.request("GET", url, headers=headers, params=querystring)
data = json.loads(response.text)

directories = [item for item in data if item['dir']]
files = [item for item in data if not item['dir']]

for item in directories:
    print(f"\033[34m{item['name']}/\033[0m")

for item in files:
    print(f"\033[32m{item['name']}\033[0m")
