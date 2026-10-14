import os
import requests
import time

TOKEN = os.getenv('TELEGRAM_TOKEN')

def send_telegram_message(message):
    if not TOKEN:
        print("Telegram Token सापडला नाही!")
        return
    
    chat_id = "1486399523"  # तुमचा अचूक चॅट आयडी येथे टाका
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

def execute_automated_session():
    print("🚀 निफ्टी लाईव्ह ऑटोमॅटिक ट्रेडिंग सत्र सुरू झाले आहे...")
    
    # सलग ३ ट्रेड्सची यादी (Market Hours Session)
    trades = [
        {"num": 1, "type": "BUY CALL (CE)", "strike": "NIFTY 25000 CE", "entry": 115.00, "target": 140.00, "sl": 95.00},
        {"num": 2, "type": "BUY PUT (PE)", "strike": "NIFTY 24900 PE", "entry": 98.00, "target": 125.00, "sl": 82.00},
        {"num": 3, "type": "BUY CALL (CE)", "strike": "NIFTY 25050 CE", "entry": 105.00, "target": 135.00, "sl": 90.00}
    ]
    
    for trade in trades:
        message = (
            f"📈 [NIFTY LIVE AUTO TRADE #{trade['num']}]\n"
            f"━━━━━━━━━━━━━━━━━━━\n"
            f"🎯 प्रकार: {trade['type']}\n"
            f"📊 स्ट्राइक: {trade['strike']}\n"
            f"💰 एंट्री: ₹{trade['entry']}\n"
            f"🎯 टार्गेट: ₹{trade['target']}\n"
            f"🛑 स्टॉपलॉस: ₹{trade['sl']}\n"
            f"⏰ मार्केट टायमिंग: लाईव्ह स्वयंचलित ट्रेड"
        )
        
        # टेलिग्रामवर मेसेज पाठवणे
        send_telegram_message(message)
        print(f"Trade {trade['num']} executed and notification sent.")
        
        # समजा तुम्हाला प्रत्येक ट्रेडमध्ये काही तासांचे किंवा मिनिटांचे अंतर हवे असेल, 
        # तर इथे वेळ सेट करू शकता (सध्या सिम्युलेशनसाठी १० सेकंद ठेवले आहे)
        if trade['num'] < 3:
            time.sleep(10)

if __name__ == "__main__":
    execute_automated_session()
    
