from pyrogram import Client, filters
from config import SOURCE_CHAT, TARGET_CHAT
from utils.telegram_client import client
from templates.edit_template import process_message
from filters import custom_filter
from loguru import logger

logger.add("logs/tracking.log", rotation="1 MB")

@client.on_message(filters.chat(SOURCE_CHAT))
def forward_message(client, message):
    logger.info(f"New message received: {message.text}")
    print(f"New message received: {message.text}")

    # First apply the filter to check if the message should be processed
    if custom_filter(message.text):
        logger.info("Message passed filter.")
        print("Message passed filter.")

        try:
            # Process the message to extract relevant content
            edited_message = process_message(message.text)
            # Forward the edited message to the target chat
            client.send_message(TARGET_CHAT, edited_message)
            logger.info(f"Message forwarded from {SOURCE_CHAT} to {TARGET_CHAT}")
            print(f"Message forwarded from {SOURCE_CHAT} to {TARGET_CHAT}")
        except Exception as e:
            # Log any errors that occur during processing or forwarding
            logger.error(f"Error processing message: {e}")
            print(f"Error processing message: {e}")
    else:
        logger.info("Message did not pass filter.")
        print("Message did not pass filter.")

if __name__ == "__main__":
    logger.info("Bot is starting...")
    print("Bot is starting...")
    client.run()
