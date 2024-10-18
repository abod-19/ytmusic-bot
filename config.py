import os
from dotenv import load_dotenv

from yt_dlp import YoutubeDL
from ytmusicapi import YTMusic

load_dotenv()

TOKEN = "7197234381:AAEYoNfw5En91ItaBhFcPRlN3zKevqhwgl0"
CHANNEL = "@IC_l9"
OWNER_ID = 5145609515

ytm = YTMusic()
ytd = YoutubeDL(
    {
        "username": "oauth2",
        "password": "",
        "format": "bestaudio",
        "outtmpl": "%(id)s.mp3",
    }
)
temp = {}


print(CHANNEL)
