# bot/handlers.py

from pyrogram import Client, filters

async def start_command(client: Client, message):
    await message.reply_text("Hello! I am your bot. How can I help you?")

async def help_command(client: Client, message):
    await message.reply_text("This is the help command. Use /start to begin.")

def register_handlers(client: Client):
    client.add_handler(filters.command("start")(start_command))
    client.add_handler(filters.command("help")(help_command))
