import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Use environment variables for sensitive information
API_KEY = os.getenv("NEKOWEB_API_KEY")
url = "https://nekoweb.org/api/files/delete"

pathname = input("Path name to file or folder for deletion: ")

payload = "pathname=" + pathname
headers = {
    "Authorization": API_KEY,
    "content-type": "application/x-www-form-urlencoded",
}

if (
    input(
        f"This will delete '{pathname}' \n\033[31mARE YOU SURE YOU WANT TO DELETE IT? (Y/N): \033[0m"
    ).lower()
    == "y"
):
    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

else:
    print("Cancelled by User.")