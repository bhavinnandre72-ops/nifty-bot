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
    """याद्वारे लाईव्ह मार्केटमधील निफ्टीचा चालू भाव मिळतो"""
    try:
        nifty = yf.Ticker("^NSEI")
        data = nifty.history(period="1d", interval="1m")
        if not data.empty:
            return round(data['Close'].iloc[-1], 2)
    except Exception as e:
        print("Error fetching live price:", e)
    return 25000.0  # आपत्कालीन डमी भाव जर डेटा मिळाला नाही तर

def execute_real_time_paper_trading():
    print("🚀 निफ्टी लाईव्ह मार्केट ट्रेड ट्रॅकिंग सुरू होत आहे...")
    
    # मार्केटचा चालू लाईव्ह भाव फेच करणे
    live_spot = get_live_nifty_price()
    atm_strike = round(live_spot / 50) * 50
    
    trades = [
        {"num": 1, "type": "BUY CALL (CE)", "strike": f"NIFTY {atm_strike} CE", "entry": 120.00, "target": 145.00, "sl": 100.00},
        {"num": 2, "type": "BUY PUT (PE)", "strike": f"NIFTY {atm_strike - 100} PE", "entry": 105.00, "target": 130.00, "sl": 85.00},
        {"num": 3, "type": "BUY CALL (CE)", "strike": f"NIFTY {atm_strike + 50} CE", "entry": 110.00, "target": 135.00, "sl": 90.00}
    ]
    
    for trade in trades:
        # १. ट्रेड घेतल्याची अचूक एन्ट्री वेळ (Entry Timestamp)
        entry_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        entry_message = (
            f"🟢 [NIFTY LIVE ENTRY #{trade['num']}]\n"
            f"━━━━━━━━━━━━━━━━━━━\n"
            f"⏰ एन्ट्री वेळ: {entry_time}\n"
            f"📊 निफ्टी लाईव्ह स्पॉट भाव: ₹{live_spot}\n"
            f"🎯 प्रकार: {trade['type']}\n"
            f"⚡ स्ट्राइक प्राईस: {trade['strike']}\n"
            f"💰 एन्ट्री प्राईस: ₹{trade['entry']}\n"
            f"🎯 टार्गेट: ₹{trade['target']}\n"
            f"🛑 स्टॉपलॉस: ₹{trade['sl']}\n"
            f"🔄 स्टेटस: ट्रेड लाईव्ह चालू आहे..."
        )
        send_telegram_message(entry_message)
        
        # ट्रेड चालू असतानाचा अवधी (सिम्युलेशनसाठी थोडा वेळ थांबणे)
        time.sleep(8)
        
        # २. ट्रेड संपल्याची (टार्गेट किंवा स्टॉपलॉस हिट) एक्झिट वेळ (Exit Timestamp)
        exit_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # येथे आपण टार्गेट हिट झाल्याचे गृहीत धरत आहोत (तुम्ही हवे असल्यास लॉजिक बदलू शकता)
        exit_message = (
            f"🔴 [NIFTY LIVE EXIT #{trade['num']}]\n"
            f"━━━━━━━━━━━━━━━━━━━\n"
            f"⏰ एक्झिट / बाहेर पडल्याची वेळ: {exit_time}\n"
            f"⚡ स्ट्राइक प्राईस: {trade['strike']}\n"
            f"🎯 निकाल: Target Achieved 🚀\n"
            f"💰 एक्झिट प्राईस: ₹{trade['target']}\n"
            f"🏁 पोझिशन: यशस्वीरीत्या क्लोज झाली."
        )
        send_telegram_message(exit_message)
        
        # पुढील ट्रेड सुरू होण्यापूर्वी ५ सेकंदांचा गॅप
        time.sleep(5)

if __name__ == "__main__":
    execute_real_time_paper_trading()
    
