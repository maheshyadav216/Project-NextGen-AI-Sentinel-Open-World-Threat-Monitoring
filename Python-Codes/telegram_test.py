import asyncio
from telegram import Bot

BOT_TOKEN = "XXXX:XXXXX"
CHAT_ID = "XXXXX"

async def send_message():

    bot = Bot(token=BOT_TOKEN)

    await bot.send_message(
        chat_id=CHAT_ID,
        text="🚨 AI Sentinel Test Alert!\nWeapon Threat Detected."
    )

asyncio.run(send_message())
