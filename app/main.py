import os
from dotenv import load_dotenv
import openai

load_dotenv('app/config/.env')

api_openai = os.getenv('api_open_ai')

openai.api_key = api_openai