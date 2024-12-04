from pyrogram import Client, filters


@app.on_message(filters.command("start"))
def start(client, message):
    message.reply("Hello, Welcome! I'm your bot.")
