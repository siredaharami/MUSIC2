import config
from pyrogram import Client
from pytgcalls import PyTgCalls, filters
from pytgcalls.types import GroupCallConfig


api_id = 12345  # Replace with your actual API ID
api_hash = "0123456789abcdef0123456789abcdef"  # Replace with your actual API Hash
bot_token = "" # Replace with your Bot-Token


app = Client(
    name="App",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    session_string=str(config.STRING_SESSION),
)

bot = Client(
    name="Bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
)

call = PyTgCalls(app)
call_config = GroupCallConfig(auto_start=False)
