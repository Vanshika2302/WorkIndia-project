from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy player statistics data (replace with actual database)
player_stats = {
    '123': {'name': 'Virat Kohli', 'matches_played': 200, 'runs': 12000, 'average': 59.8, 'strike_rate': 92.5},
    # Add more player stats as needed
}

@app.route('/api/players/<player_id>/stats', methods=['GET'])
def get_player_stats(player_id):
    # Dummy implementation, replace with actual logic to fetch player statistics
    player_stat = player_stats.get(player_id)
    if player_stat:
        return jsonify(player_stat), 200
    else:
        return jsonify({'message': 'Player stats not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
