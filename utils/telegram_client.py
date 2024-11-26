from pyrogram import Client
import config

# Create a Pyrogram Client object
client = Client(
    config.SESSION_NAME,
    api_id=config.API_ID,
    api_hash=config.API_HASH
)
