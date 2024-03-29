import pickle
from flask import Flask, jsonify
# http://localhost:4000/app

with open('Data/pokemons.pkl', 'rb') as f:
    data = pickle.load(f)


app = Flask(__name__)


# Ruta API
@app.route('/app', methods=['GET'])
def get_data():
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=4000)
