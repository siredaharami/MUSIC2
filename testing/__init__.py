# __init__.py
from pyrogram import Client, filters
from testing import app

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply("Hello! I am your bot. How can I help you?")

@app.on_message(filters.command("help"))
def help_command(client, message):
    message.reply("Available commands:\n/start - Start the bot\n/help - Show this help message")

@app.on_message(filters.text)
def echo(client, message):
    message.reply(f"You said: {message.text}")
