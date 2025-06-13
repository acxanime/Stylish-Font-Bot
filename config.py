import os
from typing import List

API_ID = os.environ.get("API_ID", "29037902")
API_HASH = os.environ.get("API_HASH", "8f963da8e2040053cf0ad8932244890e")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", "6692613520"))

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002320080278"))

DB_URI = os.environ.get("DB_URI", "mongodb+srv://Renamest:Renamest@cluster0.prfhc.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "Cluster0")

IS_FSUB = os.environ.get("IS_FSUB", "False").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-1002355394644").split()))  # Add Multiple channel id's
