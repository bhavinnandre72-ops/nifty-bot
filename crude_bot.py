import os
import requests

# GitHub Secrets मधून Telegram Token घेणे
TOKEN = os.getenv('TELEGRAM_TOKEN')

def send_telegram_message(message):
    if not TOKEN:
        print("Telegram Token सापडला नाही!")
        return
    # तुमचा चॅट आयडी येथे टाका
    chat_id = "तुमचा_Chat_ID" 
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    try:
        response = requests.post(url, json=payload)
        print("Telegram Response:", response.text)
    except Exception as e:
        print("Error sending message:", e)

if __name__ == "__main__":
    print("🛢️ Crude Oil Trading Bot सुरू झाला आहे!")
    send_telegram_message("🛢️ [CRUDE OIL BOT]\nकमोडिटी मार्केट क्रूड ऑइल ट्रेड यशस्वीपणे सुरू झाला आहे!")
