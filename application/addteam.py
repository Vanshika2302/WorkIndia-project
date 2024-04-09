from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy squad data (replace with actual database)
squads = {
    '1': [
        {'player_id': '123', 'name': 'Virat Kohli', 'role': 'Batsman'},
        {'player_id': '456', 'name': 'Jasprit Bumrah', 'role': 'Bowler'}
    ],
    # Add more squads as needed
}

@app.route('/api/teams/<team_id>/squad', methods=['POST'])
def add_player_to_squad(team_id):
    # Dummy implementation, replace with actual logic to add player to squad
    data = request.json
    player_name = data.get('name')
    player_role = data.get('role')
    player_id = str(len(squads[team_id]) + 1)  # Generate player_id (replace with actual logic)
    squads[team_id].append({'player_id': player_id, 'name': player_name, 'role': player_role})
    return jsonify({'message': 'Player added to squad successfully', 'player_id': player_id}), 200

if __name__ == '__main__':
    app.run(debug=True)
