import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Use environment variables for sensitive information
API_KEY = os.getenv('NEKOWEB_API_KEY')
url = "https://nekoweb.org/api/files/readfolder"

pathname = input("Path name to query: ")

querystring = {"pathname":pathname}

headers = {"Authorization": API_KEY}

response = requests.request("GET", url, headers=headers, params=querystring)
json = json.dumps(json.loads(response.text), indent=4)

print (json)