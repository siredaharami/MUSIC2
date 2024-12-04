from pyrogram import Client, filters 


@app.on_message(filters.command("ping"))
def ping(client, message):
    message.reply("Pong!")
