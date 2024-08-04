#!/usr/bin/python3
"""
This file contains the Amenity module
"""
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from models import storage
from models.amenity import Amenity
from flasgger.utils import swag_from


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
@swag_from('documentation/amenity/get.yml', methods=['GET'])
def get_all_amenities():
    """Retrieve all amenities"""
    amenities = [obj.to_dict() for obj in storage.all(Amenity).values()]
    return jsonify(amenities)


@app_views.route('/amenities/<string:amenity_id>', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/amenity/get_id.yml', methods=['GET'])
def get_amenity(amenity_id):
    """Retrieve a specific amenity by id"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<string:amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/amenity/delete.yml', methods=['DELETE'])
def delete_amenity(amenity_id):
    """Delete an amenity by id"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    amenity.delete()
    storage.save()
    return jsonify({})


@app_views.route('/amenities/', methods=['POST'],
                 strict_slashes=False)
@swag_from('documentation/amenity/post.yml', methods=['POST'])
def create_amenity():
    """Create a new amenity"""
    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    data = request.get_json()
    if 'name' not in data:
        return make_response(jsonify({"error": "Missing name"}), 400)
    amenity = Amenity(**data)
    amenity.save()
    return jsonify(amenity.to_dict()), 201


@app_views.route('/amenities/<string:amenity_id>', methods=['PUT'],
                 strict_slashes=False)
@swag_from('documentation/amenity/put.yml', methods=['PUT'])
def update_amenity(amenity_id):
    """Update an existing amenity"""
    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    data = request.get_json()
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(amenity, key, value)
    storage.save()
    return jsonify(amenity.to_dict())
