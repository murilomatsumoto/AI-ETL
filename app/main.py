import os
from dotenv import load_dotenv
import openai
import pandas as pd
import json
from ETL.extract import get_user
from ETL.load import update_user
from ETL.transform import generate_ai_news

load_dotenv('app/config/.env')

api_openai = os.getenv('api_open_ai')
swd2023_api_url = os.getenv('swd_url')
openai.api_key = api_openai

while True:
    print("Menu:")
    print("1. Extrair informações dos usuários")
    print("2. Implementar novas mensagens")
    print("3. Enviar mensagens para API")
    print("4. Sair")
    
    insert = input('Insira o procedimento que deseja executar (1-3): ')
    
    if insert == '1':
        print("Você escolheu a Opção 1")
        df = pd.read_csv('app/SWD2023.csv')
        user_ids = df['UserID'].tolist()
        print(user_ids)
        users = [user for id in user_ids if (user := get_user(id)) is not None]
        print(json.dumps(users, indent=2))
        
    elif insert == '2':
        print("Você escolheu a Opção 2")
        for user in users:
            news = generate_ai_news(user)
            print(f"{user['name']}, {news}")
            user['news'].append({
                "description": news
            })
        
    elif insert == '3':
        print("Você escolheu a Opção 3")
        for user in users:
            success = update_user(user)
            print(f"User  {user['name']} updated? {success}!")
            
    elif insert == '4':
        print('Saindo do programa!')
        break



# #EXTRACT
# df = pd.read_csv('app/SWD2023.csv')
# user_ids = df['UserID'].tolist()
# print(user_ids)
# users = [user for id in user_ids if (user := get_user(id)) is not None]
# print(json.dumps(users, indent=2))

# #TRANSFORM

# for user in users:
#     news = generate_ai_news(user)
#     print(f"{user['name']}, {news}")
#     user['news'].append({
#         "description": news
#     })

# #LOAD



# for user in users:
#     success = update_user(user)
#     print(f"User  {user['name']} updated? {success}!")