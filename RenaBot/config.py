import os
from telethon import TelegramClient

api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
Bot_token = os.environ.get('TOKEN')
Admin= os.environ.get('ADMIN_ID')
client=TelegramClient('bot',api_id,api_hash).start(bot_token=Bot_token)
