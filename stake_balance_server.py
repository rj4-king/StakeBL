from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/get_balance', methods=['POST'])
def get_balance():
    balances = [
        {'amount': '1.23', 'currency': 'BTC'},
        {'amount': '400.00', 'currency': 'USDT'}
    ]
    return jsonify({'balances': balances})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
