import os
import requests
import time
import yfinance as yf

TOKEN = os.getenv('TELEGRAM_TOKEN')

def send_telegram_message(message):
    if not TOKEN:
        print("Telegram Token सापडला नाही!")
        return
    
    chat_id = "1486399523"  # तुमचा टेलिग्राम चॅट आयडी
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

def get_live_nifty_price():
    """निफ्टीचा लाईव्ह स्पॉट प्राईस फेच करणे"""
    try:
        nifty = yf.Ticker("^NSEI")
        data = nifty.history(period="1d", interval="1m")
        if not data.empty:
            live_price = round(data['Close'].iloc[-1], 2)
            return live_price
    except Exception as e:
        print("Error fetching live price:", e)
    return 25000.0  # Fallback price जर API प्रतिसाद देत नसेल तर

def execute_live_paper_trading():
    print("🚀 निफ्टी लाईव्ह पेपर ट्रेडिंग सत्र सुरू होत आहे...")
    
    # १. निफ्टीचा चालू लाईव्ह भाव मिळवणे
    live_price = get_live_nifty_price()
    
    # २. चालू भावावरून जवळचा ATM स्ट्राइक शोधणे (उदा. 25012 असेल तर 25000)
    atm_strike = round(live_price / 50) * 50
    
    print(f"Nifty Live Spot Price: {live_price} | Selected ATM Strike: {atm_strike}")
    
    # ३. लाईव्ह भावावर आधारित ३ ऑप्शन्स ट्रेड्सचे सिम्युलेशन
    trades = [
        {"num": 1, "type": "BUY CALL (CE)", "strike": f"NIFTY {atm_strike} CE", "entry": 120.00, "target": 145.00, "sl": 100.00},
        {"num": 2, "type": "BUY PUT (PE)", "strike": f"NIFTY {atm_strike - 100} PE", "entry": 105.00, "target": 130.00, "sl": 85.00},
        {"num": 3, "type": "BUY CALL (CE)", "strike": f"NIFTY {atm_strike + 50} CE", "entry": 110.00, "target": 135.00, "sl": 90.00}
    ]
    
    for trade in trades:
        message = (
            f"📈 [NIFTY LIVE PAPER TRADE #{trade['num']}]\n"
            f"━━━━━━━━━━━━━━━━━━━\n"
            f"📊 निफ्टी लाईव्ह स्पॉट भाव: ₹{live_price}\n"
            f"🎯 प्रकार: {trade['type']}\n"
            f"⚡ स्ट्राइक प्राईस: {trade['strike']}\n"
            f"💰 एन्ट्री प्राईस (Estimated): ₹{trade['entry']}\n"
            f"🎯 टार्गेट: ₹{trade['target']}\n"
            f"🛑 स्टॉपलॉस: ₹{trade['sl']}\n"
            f"📦 लॉट साईज: 1 Lot (25 Qty)\n"
            f"⏰ वेळ: आजचा लाईव्ह मार्केट वेळ"
        )
        
        send_telegram_message(message)
        time.sleep(5)

if __name__ == "__main__":
    execute_live_paper_trading()
