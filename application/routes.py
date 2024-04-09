from flask import Blueprint
from werkzeug.urls import quote
from app import app
from flask import jsonify, request

@app.route('/api/admin/signup', methods=['POST'])
def register_admin():
    # Your code for registering admin
    return jsonify({'status': 'Admin Account successfully created'}), 200

routes_blueprint = Blueprint('routes', __name__)

# Define your routes here using routes_blueprint.route(...)
