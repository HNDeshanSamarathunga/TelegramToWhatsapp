import pyautogui
import time
import webbrowser

WHATSAPP_GROUP_NAME = "Bot Testing"  # Ensure the name matches your WhatsApp group exactly

def send_to_whatsapp(message):
    """Send a message to a WhatsApp group without opening a new tab."""
    try:
        print(f"🟢 Attempting to send: {message}")
        
        # Open WhatsApp Web in an existing tab
        webbrowser.open("https://web.whatsapp.com")
        time.sleep(8)  # Wait for WhatsApp Web to load
        
        # Search for the WhatsApp Group
        pyautogui.click(x=200, y=200)  # Click on the search bar (Adjust x, y if needed)
        pyautogui.write(WHATSAPP_GROUP_NAME)  # Type the group name
        time.sleep(2)
        pyautogui.press("enter")  # Open the group chat
        
        time.sleep(3)
        pyautogui.write(message)  # Type the message
        pyautogui.press("enter")  # Send the message
        
        print(f"✅ Message sent to WhatsApp group: {message}")

    except Exception as e:
        print(f"❌ Error: {e}")
