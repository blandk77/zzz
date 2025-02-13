#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
import re
from os import environ
import os

id_pattern = re.compile(r'^.\d+$')


API_ID = os.environ.get("API_ID", "26728872")
API_HASH = os.environ.get("API_HASH", "96985c2aaea6c75408528909b7e18879")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7458039455:AAGI2ANVdMNqM4gHL8hlqL1ipbm8UMCMNUM")
ADMIN = int(os.environ.get("ADMIN", '1705634892'))
FSUB_UPDATES = os.environ.get("FSUB_CHANNEL", "The_TGguy")
FSUB_GROUP = os.environ.get("FSUB_GROUP", "Tg_Guy_Support")
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://telegramguy21:tnkIwvbNkJ5U3fZ7@botsuse.bpgag.mongodb.net/?retryWrites=true&w=majority&appName=Botsuse")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster1")
CAPTION = os.environ.get("CAPTION", "{filename}")
group = environ.get('GROUP', '-1002487808073')
GROUP = int(group) if group and id_pattern.search(group) else None
#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
SUNRISES_PIC= "https://graph.org/file/89dde1d9e9fb638e3170a-5870847ced3b970b59.jpg"  # Replace with your Telegraph link
AUTH_USERS = int(os.environ.get("AUTH_USERS", '1705634892'))
WEBHOOK = bool(os.environ.get("WEBHOOK", True))
PORT = int(os.environ.get("PORT", "8080"))
LOG_CHANNEL_ID = os.environ.get("LOG_CHANNEL_ID", -1002288135729)
