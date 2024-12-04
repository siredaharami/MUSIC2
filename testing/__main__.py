from testing import app

@app.on_message()
async def handle_message(client, message):
    # Respond to text messages
    if message.text:
        await message.reply_text(f"You said: {message.text}")

if __name__ == "__main__":
    print("Bot is running...")
    app.run()
