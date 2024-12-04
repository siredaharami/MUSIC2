import os
from pyrogram import Client
from config import BOT_TOKEN, API_ID, API_HASH

# Create the Pyrogram Client
app = Client(
    "testing",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH, 
    plugins=dict(root="testing.modules")
)
