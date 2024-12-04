from pyrogram import Client, filters 
from testing import app


@app.on_message(filters.command("ping"))
def ping(client, message):
    message.reply("Pong!")
