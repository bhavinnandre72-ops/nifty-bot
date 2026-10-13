import os
import threading
from flask import Flask

# --- 1. RENDER साठी FLASK WEB SERVER ---
app = Flask(__name__)

@app.route('/')
def home():
    return "Trading Bot is Live and Running!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# --- 2. TRADING BOT LOGIC (MAX 3 TRADES) ---
max_trades = 3
trade_count = 0

def start_trading():
    global trade_count
    print("🚀 बॉट यशस्वीपणे चालू झाला आहे!")
    
    # मार्केट वेळेत ३ ट्रेड घेण्याचे लॉजिक इथे येईल
    while trade_count < max_trades:
        # तुमच्या स्ट्रॅटेजीनुसार ट्रेड कंडिशन चेक करा
        break

if __name__ == "__main__":
    # Flask ला बॅकग्राउंड थ्रेडमध्ये चालू करा (Render पोर्ट एरर टाळण्यासाठी)
    threading.Thread(target=run_flask).start()
    
    # ट्रेडिंग बॉट सुरू करा
    start_trading()
  
