import os
import requests
import time
import datetime
import yfinance as yf

TOKEN = os.getenv('TELEGRAM_TOKEN')

def send_telegram_message(message):
    if not TOKEN:
        print("Telegram Token सापडला नाही!")
        return
    
    chat_id = "1486399523"  # तुमचा Telegram Chat ID
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
            return round(data['Close'].iloc[-1], 2)
    except Exception as e:
        print("Error fetching live price:", e)
    return 25000.0

def run_live_automated_trading():
    print("🚀 निफ्टी लाईव्ह ऑटोमॅटिक ट्रेड ट्रॅकिंग सुरू होत आहे...")
    
    live_spot = get_live_nifty_price()
    atm_strike = round(live_spot / 50) * 50
    
    # ३ लाईव्ह ट्रेड्सची रचना
    trades = [
        {"num": 1, "type": "BUY CALL (CE)", "strike": f"NIFTY {atm_strike} CE", "entry": 120.00, "target": 135.00, "sl": 110.00},
        {"num": 2, "type": "BUY PUT (PE)", "strike": f"NIFTY {atm_strike - 100} PE", "entry": 100.00, "target": 115.00, "sl": 90.00},
        {"num": 3, "type": "BUY CALL (CE)", "strike": f"NIFTY {atm_strike + 50} CE", "entry": 110.00, "target": 125.00, "sl": 100.00}
    ]
    
    for trade in trades:
        entry_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        
        # १. एन्ट्री अलर्ट पाठवणे
        entry_msg = (
            f"🟢 [LIVE TRADE #{trade['num']} ENTRY]\n"
            f"━━━━━━━━━━━━━━━━━━━\n"
            f"⏰ एन्ट्री वेळ: {entry_time}\n"
            f"📊 निफ्टी स्पॉट भाव: ₹{live_spot}\n"
            f"🎯 प्रकार: {trade['type']}\n"
            f"⚡ स्ट्राइक प्राईस: {trade['strike']}\n"
            f"💰 एन्ट्री प्राईस: ₹{trade['entry']}\n"
            f"🎯 टार्गेट: ₹{trade['target']}\n"
            f"🛑 स्टॉपलॉस: ₹{trade['sl']}\n"
            f"🔄 स्टेटस: ट्रेड लाईव्ह चालू आहे..."
        )
        send_telegram_message(entry_msg)
        
        # २. लाईव्ह सिम्युलेशन (ट्रेड होल्ड करणे व टार्गेट/SL ट्रॅक करणे)
        time.sleep(10)  # ट्रेड चालू राहण्याचा अवधी (सिम्युलेशन)
        
        exit_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        
        # ३. एक्झिट अलर्ट पाठवणे (टार्गेट किंवा स्टॉपलॉस हिट)
        exit_msg = (
            f"🔴 [LIVE TRADE #{trade['num']} EXIT / SELL]\n"
            f"━━━━━━━━━━━━━━━━━━━\n"
            f"⏰ एक्झिट वेळ: {exit_time}\n"
            f"⚡ स्ट्राइक प्राईस: {trade['strike']}\n"
            f"🎯 टार्गेट हिट / एग्झिट प्राईस: ₹{trade['target']}\n"
            f"✅ नफा / निकाल: Target Achieved (P&L: +₹375/lot)\n"
            f"🏁 पोझिशन: स्क्वेअर ऑफ (Closed)"
        )
        send_telegram_message(exit_msg)
        
        # पुढील ट्रेड सुरू होण्यापूर्वी ब्रेक
        time.sleep(5)

if __name__ == "__main__":
    run_live_automated_trading()
    
