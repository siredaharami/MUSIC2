import config
from pyrogram import Client

api_id = 12345  # Replace with your actual API ID
api_hash = "0123456789abcdef0123456789abcdef"  # Replace with your actual API Hash
bot_token = "" # Replace with your Bot-Token

app = Client(
         "testing",
          api_id=config.API_ID, 
          api_hash=config.API_HASH, 
          bot_token=config.BOT_TOKEN
)
