from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/admin/signup', methods=['POST'])
def create_admin():
    # Get data from the request JSON
    data = request.get_json()

    # Extract required fields from the data
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    # Check if all required fields are present
    if not username or not password or not email:
        return jsonify({'error': 'Username, password, and email are required'}), 400

    user_id = '123445'
    response_data = {
        'status': 'Admin Account successfully created',
        'status_code': 200,
        'user_id': user_id
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
