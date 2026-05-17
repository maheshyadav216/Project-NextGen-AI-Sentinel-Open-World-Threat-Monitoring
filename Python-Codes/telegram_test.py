#=============================================================================//
# Project/Tutorial       - NextGen AI Sentinel – Open-World Threat Monitoring
# Author                 - https://www.hackster.io/maheshyadav216
# Hardware               - NVIDIA JETSON ORIN NANO SUPER DEVELOPER KIT   
# Software               - Python, OpenCV, NanoOWL
# GitHub Repo of Project - https://github.com/maheshyadav216/Project-NextGen-AI-Sentinel-Open-World-Threat-Monitoring 
# Code last Modified on  - 16/05/2026
# Code/Content license   - (CC BY-NC-SA 4.0) https://creativecommons.org/licenses/by-nc-sa/4.0/
#============================================================================//
# Telegram Bot Testing

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
#============================================================================//