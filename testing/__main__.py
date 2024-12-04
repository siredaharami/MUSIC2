import os
import importlib
from testing import app

def load_plugins():
    plugin_dir = "testing/modules"
    plugin_package = "testing.modules"

    for file_name in os.listdir(plugin_dir):
        if file_name.endswith(".py") and not file_name.startswith("__"):
            module_name = file_name[:-3]  # Remove the .py extension
            importlib.import_module(f"{plugin_package}.{module_name}")
            print(f"Successfully imported: {module_name}")

if __name__ == "__main__":
    print("Loading plugins...")
    load_plugins()
    print("All plugins imported successfully.")
    print("Bot is running...")
    app.run()



async def main():
    LOGGER.info("🐬 Updating Directories ...")
    if "cache" not in os.listdir():
        os.mkdir("cache")
    if "cookies.txt" not in os.listdir():
        LOGGER.info("⚠️ 'cookies.txt' - Not Found❗")
        sys.exit()
    if "downloads" not in os.listdir():
        os.mkdir("downloads")
    for file in os.listdir():
        if file.endswith(".session"):
            os.remove(file)
    for file in os.listdir():
        if file.endswith(".session-journal"):
            os.remove(file)
    LOGGER.info("✅ All Directories Updated.")
    await asyncio.sleep(1)
    LOGGER.info("🌐 Checking Required Variables ...")
    if API_ID == 0:
        LOGGER.info("❌ 'API_ID' - Not Found ‼️")
        sys.exit()
    if not API_HASH:
        LOGGER.info("❌ 'API_HASH' - Not Found ‼️")
        sys.exit()
    if not BOT_TOKEN:
        LOGGER.info("❌ 'BOT_TOKEN' - Not Found ‼️")
        sys.exit()
    if not STRING_SESSION:
        LOGGER.info("❌ 'STRING_SESSION' - Not Found ‼️")
        sys.exit()

    if not MONGO_DB_URL:
        LOGGER.info("'MONGO_DB_URL' - Not Found !!")
        sys.exit()
    try:
        await mongo_async_cli.admin.command('ping')
    except Exception:
        LOGGER.info("❌ 'MONGO_DB_URL' - Not Valid !!")
        sys.exit()
    LOGGER.info("✅ Required Variables Are Collected.")
    await asyncio.sleep(1)
    LOGGER.info("🌀 Starting All Clients ...")
    try:
        await bot.start()
    except Exception as e:
        LOGGER.info(f"🚫 Bot Error: {e}")
        sys.exit()
    if LOG_GROUP_ID != 0:
        try:
            await bot.send_message(LOG_GROUP_ID, "**🤖 Bot Started.**")
        except Exception:
            pass
    LOGGER.info("✅ Bot Started.")
    try:
        await app.start()
    except Exception as e:
        LOGGER.info(f"🚫 Assistant Error: {e}")
        sys.exit()
    try:
        await app.join_chat("AdityaServer")
        await app.join_chat("AdityaDiscus")
    except Exception:
        pass
    if LOG_GROUP_ID != 0:
        try:
            await app.send_message(LOG_GROUP_ID, "**🦋 Assistant Started.**")
        except Exception:
            pass
    LOGGER.info("✅ Assistant Started.")
    try:
        await call.start()
    except Exception as e:
        LOGGER.info(f"🚫 PyTgCalls Error: {e}")
        sys.exit()
    LOGGER.info("✅ PyTgCalls Started.")
    await asyncio.sleep(1)
    LOGGER.info("✅ Sucessfully Hosted Your Bot !!")
    LOGGER.info("✅ Now Do Visit: @AdityaServer !!")
    await idle()
