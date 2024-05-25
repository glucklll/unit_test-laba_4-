from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = 'https://api.exchangerate-api.com/v4/latest/USD' # Можно заменить на другой доступный API

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    amount = float(request.form['amount'])
    from_currency = request.form['from_currency']
    to_currency = request.form['to_currency']

    response = requests.get(API_URL)
    data = response.json()

    if from_currency != 'USD':
        amount_in_usd = amount / data['rates'][from_currency]
    else:
        amount_in_usd = amount

    converted_amount = amount_in_usd * data['rates'][to_currency]

    return render_template('result.html', amount=amount, from_currency=from_currency, to_currency=to_currency,
    converted_amount=converted_amount)

def main():
    app.run(debug=True)