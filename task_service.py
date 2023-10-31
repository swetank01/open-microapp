# task_service.py
from flask import Flask, jsonify
from flask_cors import CORS  # Import the CORS extension

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes in the app

tasks = [
    {"id": 1, "title": "Task 1", "user_id": 1},
    {"id": 2, "title": "Task 2", "user_id": 2},
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)
