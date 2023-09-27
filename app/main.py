import os
from dotenv import load_dotenv
import openai
import pandas as pd
import requests
import json


load_dotenv('app/config/.env')

api_openai = os.getenv('api_open_ai')
swd2023_api_url = os.getenv('swd_url')
openai.api_key = api_openai

#EXTRACT

df = pd.read_csv('app/SWD2023.csv')
user_ids = df['UserID'].tolist()
print(user_ids)

def get_user(id):
    response = requests.get(f'{swd2023_api_url}/users/{id}')
    return response.json() if response.status_code == 200 else None

users = [user for id in user_ids if (user := get_user(id)) is not None]
print(json.dumps(users, indent=2))

def generate_ai_news(user):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {'role': 'system', 'content': 'Voce é um especialista em marketing bancário'},
            {'role': 'user', 'content': f"Crie uma mensagem para {user['name']} sobre a importância dos investimentos (máximo de 100 caracteres)"}
        ]
    )
    
    return completion.choices[0].message.content.strip('\"')

# for user in users:
#     news = generate_ai_news(user)
#     print(news)
#     user['news'].append({
#         "description": news
#     })
    
# def update_user():
#     response = requests