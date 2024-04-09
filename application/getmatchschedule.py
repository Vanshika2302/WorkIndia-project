from flask import Flask, jsonify

app = Flask(__name__)

# Dummy match data (replace with actual match database)
matches = [
    {
        'match_id': '1',
        'team_1': 'India',
        'team_2': 'England',
        'date': '2023-07-10',
        'venue': "Lord's Cricket Ground"
    },
    {
        'match_id': '2',
        'team_1': 'Australia',
        'team_2': 'New Zealand',
        'date': '2023-07-11',
        'venue': 'Melbourne Cricket Ground'
    }
]

@app.route('/api/matches', methods=['GET'])
def get_match_schedules():
    # Prepare response data
    response_data = {'matches': matches}
    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(debug=True)
