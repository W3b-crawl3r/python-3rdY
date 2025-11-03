from typing import Final
import requests
from config import load_config

config = load_config()
API: Final[str] = config['api_url']
API_KEY: Final[str] = config['api_key']

def get_location(ip: str) -> dict[str, str]:
    location_response = requests.get(API + ip + '?token=' + API_KEY)
    return location_response.json()