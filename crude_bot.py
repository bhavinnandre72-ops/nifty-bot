import os
import requests
import time

TOKEN = os.getenv('TELEGRAM_TOKEN')

def send_telegram_message(message):
    if not TOKEN:
        print("Telegram Token सापडला नाही!")
        return
    
    # ⚠️ तुमचा अंकांमधील Telegram Chat ID इथे टाका
    chat_id = "1486399523" 
    
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

def execute_crude_options_trading():
    print("🛢️ Crude Oil Option Trading (Paper Trade) सुरू होत आहे...")
    
    # ३ ऑप्शन्स ट्रेड्सचे लॉजिक (CE/PE Simulation)
    trades = [
        {"type": "BUY CALL (CE)", "strike": "CRUDEOIL 6200 CE", "entry": 145.00, "target": 170.00, "sl": 130.00},
        {"type": "BUY PUT (PE)", "strike": "CRUDEOIL 6100 PE", "entry": 120.00, "target": 145.00, "sl": 105.00},
        {"type": "BUY CALL (CE)", "strike": "CRUDEOIL 6250 CE", "entry": 110.00, "target": 135.00, "sl": 95.00}
    ]
    
    for i, trade in enumerate(trades, start=1):
        message = (
            f"🛢️ [CRUDE OIL OPTION TRADE #{i}]\n"
            f"━━━━━━━━━━━━━━━━━━━\n"
            f"🎯 प्रकार: {trade['type']}\n"
            f"📊 स्ट्राइक प्राईस: {trade['strike']}\n"
            f"💰 एंट्री प्राईस: ₹{trade['entry']}\n"
            f"🎯 टार्गेट: ₹{trade['target']}\n"
            f"🛑 स्टॉपलॉस: ₹{trade['sl']}\n"
            f"📦 लॉट साईज: 1 Lot (100 Qty)\n"
            f"⏰ स्थिती: लाईव्ह ऑप्शन्स ऑर्डर प्लेस केली (Paper Trade)"
        )
        
        send_telegram_message(message)
        
        # पुढील ट्रेडसाठी ५ सेकंदांचा ब्रेक
        if i < len(trades):
            time.sleep(5)

if __name__ == "__main__":
    execute_crude_options_trading()
    
