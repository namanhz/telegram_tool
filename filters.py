def custom_filter(message_text):
    # Filter messages that contain the keyword "Alert Count"
    return "Alert Count" in message_text

print("Loading filters.py...")
