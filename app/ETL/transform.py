import openai
import os

api_openai = os.getenv('api_open_ai')
swd2023_api_url = os.getenv('swd_url')
openai.api_key = api_openai

def generate_ai_news(user):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {'role': 'system', 'content': 'Voce é um especialista em marketing bancário'},
            {'role': 'user', 'content': f"Crie uma mensagem para {user['name']} sobre a importância dos investimentos (máximo de 100 caracteres)"}
        ]
    )
    
    return completion.choices[0].message.content.strip('\"')