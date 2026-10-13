import os
import requests
import time

TOKEN = os.getenv('TELEGRAM_TOKEN')

def send_telegram_message(message):
    if not TOKEN:
        print("Telegram Token सापडला नाही!")
        return
    
    # तुमचा Telegram Chat ID इथे टाка
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

def execute_paper_trading():
    print("🛢️ क्रूड ऑइल पेपर ट्रेडिंग (Demo Trade) सुरू होत आहे...")
    
    # सलग ३ ट्रेड घेण्याचे लॉजिक
    for i in range(1, 4):
        # डमी डेटा किंवा सिम्युलेटेड प्राईस (उदा. क्रूड ऑइलचा भाव)
        simulated_price = 6150.00 + (i * 10)
        
        trade_message = (
            f"🛢️ [CRUDE OIL PAPER TRADE #{i}]\n"
            f"━━━━━━━━━━━━━━━━━━━\n"
            f"📊 स्टेटस: यशस्वीरित्या प्लेस झाला (Demo)\n"
            f"📈 सिम्बॉल: CRUDEOIL FUT\n"
            f"💵 प्राईस: ₹{simulated_price}\n"
            f"🔢 लॉट: 1 (Paper Trading)\n"
            f"⏰ वेळ: लाइव्ह सिम्युलेशन"
        )
        
        # टेलिग्रामवर मेसेज पाठवणे
        send_telegram_message(trade_message)
        
        # पुढचा ट्रेड घेण्यापूर्वी ५ सेकंदांचे अंतर ठेवणे
        if i < 3:
            time.sleep(5)

if __name__ == "__main__":
    execute_paper_trading()
    
