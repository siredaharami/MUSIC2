import asyncio
from pyrogram import Client, filters
from testing import app

# Define the '/start' command handler
@app.on_message(filters.command("start"))
async def start(client, message):
    # Send a welcome message when the user sends the /start command
    await message.reply("Hello! Welcome to the bot. How can I assist you today?")
