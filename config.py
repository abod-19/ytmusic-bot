import os
from dotenv import load_dotenv

from yt_dlp import YoutubeDL
from ytmusicapi import YTMusic

load_dotenv()

TOKEN = os.environ.get("7197234381:AAEYoNfw5En91ItaBhFcPRlN3zKevqhwgl0")
CHANNEL = "@" + os.environ.get("IC_l9", "")
OWNER_ID = int(os.environ.get("5145609515", 1))

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
