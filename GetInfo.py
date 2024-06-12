import requests
import json
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

username = input("Enter the username to get info for: ")

API_KEY = os.getenv("NEKOWEB_API_KEY")
url = f"https://nekoweb.org/api/site/info/{username}"

headers = {
    "Authorization": API_KEY,
}

response = requests.request("GET", url, headers=headers)
data = json.loads(response.text)

if data == {"error": "Site not found"}:
    print("\033[48;5;1mError: Site not found", "\033[0m")
    exit(1)


created_at = datetime.fromtimestamp(data["created_at"] / 1000).strftime(
    "%Y-%m-%d %H:%M:%S"
)
updated_at = datetime.fromtimestamp(data["updated_at"] / 1000).strftime(
    "%Y-%m-%d %H:%M:%S"
)

for key, value in data.items():
    if key not in ["created_at", "updated_at"]:
        print(f"\033[34m{key}\033[0m: \033[33m{value}\033[0m")

print("\033[34mCreated on\033[0m:\033[33m", created_at, "\033[0m")
print("\033[34mUpdated on\033[0m:\033[33m", updated_at, "\033[0m")
