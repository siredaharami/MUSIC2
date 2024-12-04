# __init__.py

import os
import importlib
from pyrogram import Client

# Replace 'my_bot' with your bot's name and 'API_ID' and 'API_HASH' with your credentials
API_ID = '12380656'
API_HASH = 'd927c13beaaf5110f25c505b7c071273'
BOT_TOKEN = '7016394451:AAHVzndz5nyaH5xQ-oOu_Z6tOX3c3Uumd4A'

# Create a Pyrogram Client
bot = Client("testing", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Function to load all modules from the modules folder
def load_modules():
    modules_dir = os.path.dirname(__file__) + "/modules"
    for filename in os.listdir(modules_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]  # Remove .py extension
            importlib.import_module(f"testing.modules.{module_name}")

# Load all modules
load_modules()
