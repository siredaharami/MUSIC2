import os
from pytgcalls.types import GroupCallConfig
from pytgcalls import PyTgCalls
from pyrogram import Client
from config import BOT_TOKEN, API_ID, API_HASH, STRING_SESSION

# Create the Pyrogram Client
bot = Client(
    name="testing",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)


app = Client(
    name="App",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=str(STRING_SESSION),
)

call = PyTgCalls(app)
call_config = GroupCallConfig(auto_start=False)
