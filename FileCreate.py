import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Use environment variables for sensitive information
API_KEY = os.getenv("NEKOWEB_API_KEY")
url = "https://nekoweb.org/api/files/create"

headers = {
    "Authorization": API_KEY,
    "content-type": "application/x-www-form-urlencoded",
}

# Directly validate the isFolder input
isFolder = input("Is this a folder (true/false): ").lower()
while isFolder not in ["true", "false"]:
    print("Invalid input (true or false)")
    isFolder = input("This is a folder (true/false): ").lower()

# Directly validate the pathname input
pathname = input("File/Folder name (no spaces): ")
while " " in pathname:
    print("Invalid input (no spaces)")
    pathname = input("File/Folder name (no spaces): ")


payload = {"isFolder": isFolder, "pathname": pathname}

try:
    response = requests.post(url, data=payload, headers=headers)
    response.raise_for_status()  # Raises an HTTPError if the response status code is 4xx or 5xx
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
