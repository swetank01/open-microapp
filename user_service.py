from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_cors import CORS  # Import the CORS extension

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes in the app

# Set up JWT
app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # Change this to a long, random string in production
jwt = JWTManager(app)

# User data (for demonstration purposes)
users = [
    {"id": 1, "username": "user1", "password": "password1"},
    {"id": 2, "username": "user2", "password": "password2"}
]

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Check if username already exists (in a real application, you'd check a database)
    if any(user['username'] == username for user in users):
        return jsonify({"message": "Username already exists"}), 400

    # Add the new user (in a real application, you'd save this to a database)
    new_user = {"id": len(users) + 1, "username": username, "password": password}
    users.append(new_user)

    return jsonify({"message": "User registered successfully"}), 201

# User login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Check if username and password match (in a real application, you'd check a database)
    user = next((user for user in users if user['username'] == username and user['password'] == password), None)
    if user:
        # Create an access token
        access_token = create_access_token(identity=user['id'])
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

# Protected endpoint (requires valid JWT)
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

