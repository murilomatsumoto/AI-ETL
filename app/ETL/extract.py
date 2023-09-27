import pandas as pd
import requests
import json
from dotenv import load_dotenv
import os
import openai


load_dotenv('app/config/.env')

api_openai = os.getenv('api_open_ai')
swd2023_api_url = os.getenv('swd_url')
openai.api_key = api_openai


df = pd.read_csv('app/SWD2023.csv')
user_ids = df['UserID'].tolist()
print(user_ids)

def get_user(id):
    response = requests.get(f'{swd2023_api_url}/users/{id}')
    return response.json() if response.status_code == 200 else None

