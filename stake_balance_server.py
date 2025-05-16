from flask import Flask, request, jsonify
from stake_api import Stake
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/get_balance', methods=['POST'])
def get_balance():
    api_key = request.json.get('api_key')
    if not api_key:
        return jsonify({'error': 'API Key required'}), 400
    try:
     stake = Stake(api_key)
response = stake.user_balances()
balances = []
for currency in response['data']['user']['balances']:
    balances.append({
        'amount': currency['available']['amount'],
        'currency': currency['available']['currency'].upper()
    })
return jsonify({'balances': balances})

# This is FAKE demo data, not real balance!
balances = [
    {'amount': '1.23', 'currency': 'BTC'},
    {'amount': '400.00', 'currency': 'USDT'}
]
return jsonify({'balances': balances})





    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
