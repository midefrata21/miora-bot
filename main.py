from flask import Flask
import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

app = Flask(__name__)

@app.route("/send-signal")
def send_signal():
    message = """
🚨 SINYAL SCALPING BTC (Auto BingX)
Pair : BTC/USDT
Harga Sekarang : 66,420
Sinyal : 🔻 SELL
Harga Entry : 66,400
Stop Loss : 66,600
Take Profit : 65,900
Akurasi Persentase Profit : 80%
Alasan : Harga menyentuh resistance + RSI jenuh beli
Leverage: 10x
Gunakan juga resistance dan titik support sebagai acuan BUY/SELL.
"""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)
    return "Sinyal berhasil dikirim ke Telegram!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
