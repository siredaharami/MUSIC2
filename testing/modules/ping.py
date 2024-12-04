import time
import psutil
import platform
from testing import app
from pyrogram import filters

# Record the bot's start time
BOT_START_TIME = time.time()

def get_readable_time(seconds: int) -> str:
    """Convert seconds to a readable time format (Days, Hours, Minutes, Seconds)."""
    count = seconds
    days = count // (24 * 3600)
    count %= 24 * 3600
    hours = count // 3600
    count %= 3600
    minutes = count // 60
    count %= 60
    return f"{days}d {hours}h {minutes}m {count}s"

@app.on_message(filters.command("ping"))
async def ping_command(client, message):
    # Measure response time
    start_time = time.time()
    reply = await message.reply_text("Pinging...")
    end_time = time.time()
    ping_time = (end_time - start_time) * 1000

    # Calculate uptime
    uptime = get_readable_time(int(time.time() - BOT_START_TIME))

    # System stats
    cpu_usage = psutil.cpu_percent()
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    system_info = platform.system() + " " + platform.release()

    # Advanced response
    response_text = (
        f"🏓 **Pong!**\n\n"
        f"📡 **Response Time:** `{ping_time:.2f} ms`\n"
        f"⏱ **Uptime:** `{uptime}`\n"
        f"🖥 **System Info:** `{system_info}`\n"
        f"⚙️ **CPU Usage:** `{cpu_usage}%`\n"
        f"💾 **Memory Usage:** `{memory_usage}%`"
    )
    await reply.edit_text(response_text)
