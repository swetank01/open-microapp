# user_service.py
from flask import Flask, jsonify
from flask_cors import CORS  # Import the CORS extension

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes in the app

users = [
    {"id": 1, "name": "User 1"},
    {"id": 2, "name": "User 2"},
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)