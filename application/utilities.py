# utilities.py

from MySQLdb import DBAPISet
from application.models import Match, Player
from . import db
from werkzeug.urls import quote



def generate_match_summary(match_id):
    """
    Generates a summary of a given match.
    
    Parameters:
    - match_id: ID of the match.
    
    Returns:
    - Summary string describing the match.
    """
    match = Match.query.get(match_id)
    if not match:
        return "Match not found"
    
    summary = f"Match: {match.team1} vs {match.team2}\n"
    summary += f"Venue: {match.venue}\n"
    summary += f"Date: {match.date}\n"
    summary += f"Result: {match.result}\n"
    
    return summary

def update_player_stats(player_id, stats):
    """
    Updates the statistics of a player.
    
    Parameters:
    - player_id: ID of the player whose stats to update.
    - stats: Dictionary containing the updated stats.
      Example: {'runs': 50, 'wickets': 2, 'catches': 1}
    
    Returns:
    - Boolean indicating success or failure of the update operation.
    """
    player = Player.query.get(player_id)
    if not player:
        return False
    
    # Update player stats
    if 'runs' in stats:
        player.runs += stats['runs']
    if 'wickets' in stats:
        player.wickets += stats['wickets']
    if 'catches' in stats:
        player.catches += stats['catches']
    
    # Commit changes to the database
    db.session.commit()
    
    return True
