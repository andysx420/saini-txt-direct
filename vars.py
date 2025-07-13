# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "22632693"))
API_HASH = environ.get("API_HASH", "44e5cc6bbd184e43c0d6d41a939f342d")
BOT_TOKEN = environ.get("BOT_TOKEN", "7683063994:AAEkM7wMwC1VUilHGJxs72CzCXbxaf4PAdA")
OWNER = int(environ.get("OWNER", "1615865254"))
CREDIT = environ.get("CREDIT", "ANDYSX")
AUTH_USER = os.environ.get('AUTH_USERS', '1615865254').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
