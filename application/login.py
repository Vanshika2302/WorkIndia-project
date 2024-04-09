from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy user data (replace with actual user database)
users = {
    'example_user': {
        'password': 'example_password',
        'user_id': '12345'
    }
}

@app.route('/api/admin/login', methods=['POST'])
def login():
    # Get data from the request JSON
    data = request.get_json()

    # Extract username and password from the data
    username = data.get('username')
    password = data.get('password')

    # Check if username exists and password matches
    if username in users and users[username]['password'] == password:
        # Return success response with user_id and access_token
        response_data = {
            'status': 'Login successful',
            'status_code': 200,
            'user_id': users[username]['user_id'],
            'access_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'  # Dummy access token
        }
    else:
        # Return error response for incorrect username/password
        response_data = {
            'status': 'Incorrect username/password provided. Please retry',
            'status_code': 401
        }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
