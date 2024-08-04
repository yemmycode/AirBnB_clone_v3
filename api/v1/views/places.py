#!/usr/bin/python3
"""
This file contains the Place module
"""
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from models import storage
from models.place import Place
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.state import State
from flasgger.utils import swag_from

@app_views.route('/cities/<string:city_id>/places', methods=['GET'], strict_slashes=False)
@swag_from('documentation/places/get.yml', methods=['GET'])
def get_all_places(city_id):
    """List all places in a specific city by its ID."""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    return jsonify([place.to_dict() for place in city.places])

@app_views.route('/places/<string:place_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/places/get_id.yml', methods=['GET'])
def get_place(place_id):
    """Get a specific place by its ID."""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    return jsonify(place.to_dict())

@app_views.route('/places/<string:place_id>', methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/places/delete.yml', methods=['DELETE'])
def delete_place(place_id):
    """Delete a specific place by its ID."""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    place.delete()
    storage.save()
    return jsonify({})

@app_views.route('/cities/<string:city_id>/places', methods=['POST'], strict_slashes=False)
@swag_from('documentation/places/post.yml', methods=['POST'])
def create_place(city_id):
    """Create a new place instance in a specific city."""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    json_data = request.get_json()
    if 'user_id' not in json_data:
        return make_response(jsonify({"error": "Missing user_id"}), 400)
    if 'name' not in json_data:
        return make_response(jsonify({"error": "Missing name"}), 400)
    json_data['city_id'] = city_id
    user = storage.get(User, json_data['user_id'])
    if user is None:
        abort(404)
    place = Place(**json_data)
    place.save()
    return jsonify(place.to_dict()), 201

@app_views.route('/places/<string:place_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/places/put.yml', methods=['PUT'])
def update_place(place_id):
    """Update a place by its ID."""
    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    json_data = request.get_json()
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    for key, value in json_data.items():
        if key not in ['id', 'user_id', 'city_id', 'created_at', 'updated']:
            setattr(place, key, value)
    storage.save()
    return jsonify(place.to_dict())

@app_views.route('/places_search', methods=['POST'], strict_slashes=False)
@swag_from('documentation/places/search.yml', methods=['POST'])
def search_places():
    """Search for places based on various filters."""
    json_data = request.get_json()
    if json_data is None:
        return make_response(jsonify({"error": "Not a JSON"}), 400)

    states = json_data.get('states', [])
    cities = json_data.get('cities', [])
    amenities = json_data.get('amenities', [])

    if not states and not cities and not amenities:
        places = [place.to_dict() for place in storage.all(Place).values()]
        return jsonify(places)

    filtered_places = []

    if states:
        for state_id in states:
            state = storage.get(State, state_id)
            if state:
                for city in state.cities:
                    if city:
                        filtered_places.extend(city.places)

    if cities:
        for city_id in cities:
            city = storage.get(City, city_id)
            if city:
                for place in city.places:
                    if place not in filtered_places:
                        filtered_places.append(place)

    if amenities:
        if not filtered_places:
            filtered_places = storage.all(Place).values()
        amenities_objects = [storage.get(Amenity, a_id) for a_id in amenities]
        filtered_places = [place for place in filtered_places
                           if all(amenity in place.amenities for amenity in amenities_objects)]

    result = [place.to_dict() for place in filtered_places]
    for place in result:
        place.pop('amenities', None)

    return jsonify(result)
