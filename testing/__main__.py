import asyncio
from pyrogram import idle
from testing import bot # Import the app from init.py
from pyrogram import filters

async def main():
    async with bot:
    
        print("Bot is running...")

        await bot.idle()  # Keep the bot running
        
if __name__ == "__main__":
    bot.run()
