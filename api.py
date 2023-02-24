import pickle
from flask import Flask, jsonify


with open('Data/pokemons.pkl', 'rb') as f:
    data = pickle.load(f)


api = Flask(__name__)


# Ruta API
@app.route('/api', methods=['GET'])
def get_data():
    return jsonify(data)


if __name__ == '__main__':
    api.run(debug=True, port=4000)
