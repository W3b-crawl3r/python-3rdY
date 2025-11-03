
from typing import Final
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API:Final[str] = "https://ipinfo.io/"
API_KEY:Final[str] = os.environ.get('API_KEY', '')

def get_location(ip: str) -> dict[str, str]:
    location_response = requests.get(API + ip + '?token=' + API_KEY)
    return location_response.json()