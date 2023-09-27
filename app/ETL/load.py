
import requests
from dotenv import load_dotenv
import os
import openai


load_dotenv('app/config/.env')

api_openai = os.getenv('api_open_ai')
swd2023_api_url = os.getenv('swd_url')
openai.api_key = api_openai

def update_user(user):
    response = requests.put(f"{swd2023_api_url}/users/{user['id']}", json=user)
    return True if response.status_code == 200 else False