from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy match data (replace with actual match database)
matches = []

@app.route('/api/matches', methods=['POST'])
def create_match():
    # Get Authorization token from headers
    authorization_header = request.headers.get('Authorization')
    if not authorization_header or not authorization_header.startswith('Bearer '):
        return jsonify({'error': 'Authorization token missing or invalid'}), 401
    
    # Extract token from header
    token = authorization_header.split(' ')[1]

    # Dummy authentication (replace with actual authentication mechanism)
    if token != 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9':
        return jsonify({'error': 'Invalid token'}), 401

    # Get data from the request JSON
    data = request.get_json()

    # Extract match details from the data
    team_1 = data.get('team_1')
    team_2 = data.get('team_2')
    date = data.get('date')
    venue = data.get('venue')

    # Add match to the matches list
    match_id = len(matches) + 1
    match = {
        'match_id': str(match_id),
        'team_1': team_1,
        'team_2': team_2,
        'date': date,
        'venue': venue
    }
    matches.append(match)

    # Return success response with match_id
    response_data = {
        'message': 'Match created successfully',
        'match_id': str(match_id)
    }
    return jsonify(response_data), 201

if __name__ == '__main__':
    app.run(debug=True)
