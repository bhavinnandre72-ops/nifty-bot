from datetime import datetime
import time
import requests

TOKEN = "8667131376:AAFRsq79krKkfHr8OFzD0cVh6vooie6jYcI"
CHAT_ID = "1486399523"


def send_telegram_message(message):
  url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
  payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
  try:
    response = requests.post(url, json=payload)
    return response.json()
  except Exception as e:
    print(f"Error: {e}")


now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
init_msg = (
    f"🤖 *Bhavin Trading Bot - Render Active*\n\n"
    f"⏱ *Time:* `{now_str}`\n"
    f"💰 *Capital Limit:* ₹10,000 (1 Lot / 65 Units)\n"
    f"📊 *Market Hours:* 09:15 AM - 03:30 PM (Mon - Fri)\n"
    f"🎯 *Daily Target:* 3 Trades Automatic\n\n"
    f"सिस्टीम क्लाउडवर यशस्वीपणे सुरू झाली आहे!"
)
send_telegram_message(init_msg)

last_checked_day = None
trade_1_done = False
trade_2_done = False
trade_3_done = False

while True:
  now = datetime.now()
  current_time = now.time()
  current_day = now.weekday()
  today_date = now.date()

  if last_checked_day != today_date:
    trade_1_done = False
    trade_2_done = False
    trade_3_done = False
    last_checked_day = today_date

  if current_day < 5:
    market_start = datetime.strptime("09:15:00", "%H:%M:%S").time()
    market_end = datetime.strptime("15:30:00", "%H:%M:%S").time()

    if market_start <= current_time <= market_end:
      time_str = current_time.strftime("%H:%M")

      if time_str == "09:30" and not trade_1_done:
        msg = (
            f"📈 *ऑटोमॅटिक ट्रेड अलर्ट (1/3) - {today_date}*\n\n"
            f"🎯 *सिग्नल:* NIFTY 22500 CE\n"
            f"💰 *प्रिमियम भाव:* ₹90.0\n"
            f"📦 *गुंतवणूक:* ₹5,850.0 (65 Units)\n"
            f"🛑 *स्टॉप लॉस:* ₹75.0\n"
            f"🎯 *टार्गेट:* ₹120.0\n\n"
            f"⏱ *वेळ:* `{datetime.now().strftime('%H:%M:%S')}`"
        )
        send_telegram_message(msg)
        trade_1_done = True

      elif time_str == "11:30" and not trade_2_done:
        msg = (
            f"📈 *ऑटोमॅटिक ट्रेड अलर्ट (2/3) - {today_date}*\n\n"
            f"🎯 *सिग्नल:* NIFTY 22600 CE\n"
            f"💰 *प्रिमियम भाव:* ₹95.0\n"
            f"📦 *गुंतवणूक:* ₹6,175.0 (65 Units)\n"
            f"🛑 *स्टॉप लॉस:* ₹80.0\n"
            f"🎯 *टार्गेट:* ₹125.0\n\n"
            f"⏱ *वेळ:* `{datetime.now().strftime('%H:%M:%S')}`"
        )
        send_telegram_message(msg)
        trade_2_done = True

      elif time_str == "13:30" and not trade_3_done:
        msg = (
            f"📈 *ऑटोमॅटिक ट्रेड अलर्ट (3/3) - {today_date}*\n\n"
            f"🎯 *सिग्नल:* NIFTY 22450 PE\n"
            f"💰 *प्रिमियम भाव:* ₹88.0\n"
            f"📦 *गुंतवणूक:* ₹5,720.0 (65 Units)\n"
            f"🛑 *स्टॉप लॉस:* ₹73.0\n"
            f"🎯 *टार्गेट:* ₹118.0\n\n"
            f"⏱ *वेळ:* `{datetime.now().strftime('%H:%M:%S')}`"
        )
        send_telegram_message(msg)
        trade_3_done = True

  time.sleep(60)
  
