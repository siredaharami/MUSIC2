import asyncio
import importlib
import sys 
from pyrogram import idle
from testing.modules import ALL_MODULES
from testing import app  # Import the app from init.py
from pyrogram import filters

async def main():
    async with app:
        await app.start()
        for all_module in ALL_MODULES:
        importlib.import_module("testing.modules" + all_module)
        LOGGER("testing.modules").info(
        "Successfully Imported Modules"
        )
        print("Bot is running...")
        await app.idle()  # Keep the bot running
        
if __name__ == "__main__":
    asyncio.run(main())
