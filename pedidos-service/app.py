from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/pedido', methods=['POST'])
def pedido():

    return jsonify({
        "mensaje": "Pedido realizado correctamente"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)