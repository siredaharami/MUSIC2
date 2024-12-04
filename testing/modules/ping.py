from pyrogram import Client, filters 


@Client.on_message(filters.command("ping"))
def ping(client, message):
    message.reply("Pong!")
