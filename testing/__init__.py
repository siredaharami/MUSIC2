# bot/__init__.py

from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from testing.handlers import register_handlers

class MyTelegramBot(Client):
    def __init__(self):
        super().__init__("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
        register_handlers(self)

    def run(self):
        self.start()
        print("Bot is running...")
        self.idle()  # Keep the bot running until you press Ctrl+C
