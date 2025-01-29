import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

MONGODB_URI = os.getenv('MONGODB_URI')
MONGODB_DB = os.getenv('MONGODB_DB')

if not isinstance(MONGODB_URI, str) or not isinstance(MONGODB_DB, str):
    raise ValueError("Environment variables MONGODB_URI and MONGODB_DB must be strings")
