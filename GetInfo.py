import requests
import json
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

username = input("Username: ")

API_KEY = os.getenv('NEKOWEB_API_KEY')
url = "https://nekoweb.org/api/site/info/" + username

headers = {"Authorization": API_KEY,}

response = requests.request("GET", url, headers=headers)
data = json.loads(response.text)

created_at = datetime.fromtimestamp(data['created_at'] / 1000).strftime('%Y-%m-%d %H:%M:%S')
updated_at = datetime.fromtimestamp(data['updated_at'] / 1000).strftime('%Y-%m-%d %H:%M:%S')

# Print the modified data
formatted_json = json.dumps(data, indent=4)
colorful_json = highlight(formatted_json, JsonLexer(), TerminalFormatter())

print(colorful_json)
print("Created at:", created_at)
print("Updated at:", updated_at)
