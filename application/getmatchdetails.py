from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy match data (replace with actual match database)
matches = [
    {
        'match_id': '1',
        'team_1': 'India',
        'team_2': 'England',
        'date': '2023-07-10',
        'venue': "Lord's Cricket Ground",
        'status': 'upcoming',
        'squads': {
            'team_1': [
                {'player_id': '123', 'name': 'Virat Kohli'},
                {'player_id': '456', 'name': 'Jasprit Bumrah'}
            ],
            'team_2': [
                {'player_id': '789', 'name': 'Joe Root'},
                {'player_id': '101', 'name': 'Ben Stokes'}
            ]
        }
    },
    # Add more match data as needed
]

@app.route('/api/matches/<match_id>', methods=['GET'])
def get_match_details(match_id):
    # Find the match with the given match_id
    match = next((m for m in matches if m['match_id'] == match_id), None)
    if match:
        return jsonify(match), 200
    else:
        return jsonify({'message': 'Match not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
