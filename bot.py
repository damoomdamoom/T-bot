
from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8105488886:AAHvxd_90UNHivZjfy58sTZyfpXhyOl0W1w"
CHAT_ID = "7239312119"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    message = data.get('message', '📢 إشارة جديدة من TradingView')
    send_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(send_url, json=payload)
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
