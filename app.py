from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

# List of supported coins
supported_coins = ["BTC", "ETH", "BNB", "TON", "DOGE", "PEPE", "SHIB", "SUN", "TRX"]

# Wallet model
wallet = {coin: 0 for coin in supported_coins}

# API to fetch prices
def fetch_prices():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,binancecoin,toncoin,dogecoin,pepecoin,shiba-inu,sun-token,tron&vs_currencies=usd"
    response = requests.get(url)
    return response.json()

@app.route('/')
def index():
    prices = fetch_prices()
    return render_template('index.html', prices=prices)

@app.route('/wallet')
def wallet_view():
    return render_template('wallet.html', wallet=wallet)

@app.route('/deposit', methods=['POST'])
def deposit():
    coin = request.form.get('coin')
    amount = float(request.form.get('amount'))
    if coin in wallet:
        wallet[coin] += amount
    return redirect(url_for('wallet_view'))

@app.route('/withdraw', methods=['POST'])
def withdraw():
    coin = request.form.get('coin')
    amount = float(request.form.get('amount'))
    if coin in wallet and wallet[coin] >= amount:
        wallet[coin] -= amount
    return redirect(url_for('wallet_view'))

@app.route('/trade', methods=['POST'])
def trade():
    # Trading logic can be added here
    return "Trade functionality is not yet implemented"

if __name__ == '__main__':
    app.run(debug=True)
