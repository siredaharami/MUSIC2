import asyncio
import os
import importlib
from testing import bot, app

async def main():
    plugin_dir = "testing/modules"
    plugin_package = "testing.modules"

    for file_name in os.listdir(plugin_dir):
        if file_name.endswith(".py") and not file_name.startswith("__"):
            module_name = file_name[:-3]  # Remove the .py extension
            importlib.import_module(f"{plugin_package}.{module_name}")
            print(f"Successfully imported: {module_name}")
            await bot.start() 
            await app.start() 
            await idle()


if __name__ == "__main__":
    print("Loading plugins...")
    load_plugins()
    print("All plugins imported successfully.")
    print("Bot is running...")
