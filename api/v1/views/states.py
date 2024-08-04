#!/usr/bin/python3
"""State module"""
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from models import storage
from models.state import State
from flasgger.utils import swag_from

@app_views.route('/states', methods=['GET'], strict_slashes=False)
@swag_from('documentation/state/get.yml', methods=['GET'])
def get_all_states():
    """Retrieve all states"""
    states = [state.to_dict() for state in storage.all(State).values()]
    return jsonify(states)

@app_views.route('/states/<string:state_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/state/get_id.yml', methods=['GET'])
def get_state_by_id(state_id):
    """Retrieve a state by ID"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    return jsonify(state.to_dict())

@app_views.route('/states/<string:state_id>', methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/state/delete.yml', methods=['DELETE'])
def delete_state(state_id):
    """Delete a state by ID"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    state.delete()
    storage.save()
    return jsonify({})

@app_views.route('/states', methods=['POST'], strict_slashes=False)
@swag_from('documentation/state/post.yml', methods=['POST'])
def create_state():
    """Create a new state"""
    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    if 'name' not in request.get_json():
        return make_response(jsonify({"error": "Missing name"}), 400)
    data = request.get_json()
    new_state = State(**data)
    new_state.save()
    return jsonify(new_state.to_dict()), 201

@app_views.route('/states/<string:state_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/state/put.yml', methods=['PUT'])
def update_state(state_id):
    """Update an existing state"""
    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict())
