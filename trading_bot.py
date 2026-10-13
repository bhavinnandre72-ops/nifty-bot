import os
import requests

# GitHub Secrets मधून Telegram Token घेणे
TOKEN = os.getenv('TELEGRAM_TOKEN')

def send_telegram_message(message):
    if not TOKEN:
        print("Telegram Token सापडला नाही!")
        return
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": "1486399523",  # किंवा तुमचा Chat ID
        "text": message
    }
    try:
        response = requests.post(url, json=payload)
        print("Telegram Response:", response.text)
    except Exception as e:
        print("Error sending message:", e)

if __name__ == "__main__":
    print("🚀 Nifty Trading Bot सुरू झाला आहे!")
    send_telegram_message("🤖 Nifty Trading Bot यशस्वीपणे सुरू झाला आणि ट्रेड प्रक्रिया चालू आहे!")
  
