from telethon import TelegramClient, events
from whatsapp_forwarder import send_to_whatsapp  # Import the function

# Telegram API Credentials
API_ID = 2Bot Testing
Hi
0117409  # Replace with your actual API_ID
API_HASH = "ee15dadf487c01c12d912aff11bbe66f"  # Replace with your actual API_HASH
PHONE_NUMBER = "+94761933304"  # Replace with your actual phone number
CHANNEL_USERNAME = "TTWBotTest01"  # If it's private, use the Channel ID (-100xxxxxxxxx)

# Initialize Telegram Client
client = TelegramClient("session_name", API_ID, API_HASH)

@client.on(events.NewMessage(chats=CHANNEL_USERNAME))
async def new_message_listener(event):
    """Listen for new messages in the Telegram channel and display them in the terminal."""
    message = event.message.message
    print(f"\n📩 New Message from {CHANNEL_USERNAME}: {message}")

    # Forward message to WhatsApp
    send_to_whatsapp(message)Hello, this is a test message from Python!
    

async def main():
    await client.start(PHONE_NUMBER)
    
    # Confirm login
    me = await client.get_me()
    if me:
        print(f"✅ Logged in as: {me.username}")
    else:
        print("❌ Login failed! Check your API credentials.")
        return

    print(f"✅ Listening for messages from {CHANNEL_USERNAME}... Waiting for updates!")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
