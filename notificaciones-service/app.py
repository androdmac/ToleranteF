from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/Notificaciones')
def Notificaciones():

    return jsonify({
        "mensaje": "Nueva Notificacion"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)