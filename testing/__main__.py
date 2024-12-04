import asyncio
from pyrogram import idle
from testing import app # Import the app from init.py
from pyrogram import filters

async def main():
    async with app:
    
        print("Bot is running...")

        await app.idle()  # Keep the bot running
        
if __name__ == "__main__":
    app.run()
