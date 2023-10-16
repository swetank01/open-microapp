# user_service.py
from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "User 1"},
    {"id": 2, "name": "User 2"},
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(port=5000)