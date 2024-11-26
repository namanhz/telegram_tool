import os
from dotenv import load_dotenv

# Load sensitive data from the .env file
load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
SESSION_NAME = os.getenv("SESSION_NAME")
SOURCE_CHAT = os.getenv("SOURCE_CHAT")  # The chat ID or username of the source
TARGET_CHAT = os.getenv("TARGET_CHAT")  # The chat ID or username of the destination

# Debugging tip: Print the variables to see if they load correctly
if not API_ID or not API_HASH or not SESSION_NAME or not SOURCE_CHAT or not TARGET_CHAT:
    print("One or more environment variables are not set correctly in the .env file.")
