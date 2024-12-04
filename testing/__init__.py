import config
from pyrogram import Client
from pytgcalls import PyTgCalls, filters
from pytgcalls.types import GroupCallConfig


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

# Bot Client
app = Client()

# Assistant Client
bot = Client()
