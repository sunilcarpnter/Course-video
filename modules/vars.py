#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "33880368"))
API_HASH = environ.get("API_HASH", "d4a75dd7620aabcd07a38e805179ac42")
BOT_TOKEN = environ.get("BOT_TOKEN", "8529241793:AAEczt_8P3G6gx7E_rV5zEzSvxf_jL3kytA")

OWNER = int(environ.get("OWNER", "1785431143"))
CREDIT = environ.get("CREDIT", "SONU")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '1785431143').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '1785431143').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))



