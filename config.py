import os
import re
import sys
from os import getenv
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# You can add more configuration variables as needed