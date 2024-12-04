from pyrogram import Client, idle
import os
import config
from config import API_ID, API_HASH, BOT_TOKEN

# Create the bot instance
app = Client(
    "testing",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    plugins=dict(root="testing.modules")  # Point to the plugins folder
)

# Start the bot
if __name__ == "__main__":
    print("Bot is starting...")
    app.start()
    print("Bot is running. Press Ctrl+C to stop.")
    idle()  # Keep the bot running until interrupted
    app.stop()
    print("Bot stopped.")
