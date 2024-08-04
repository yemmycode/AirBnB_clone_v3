#!/usr/bin/python3
"""
This module contains the principal application
"""
from models import storage
from api.v1.views import app_views
from flask import Flask, make_response, jsonify
from os import getenv
from flask_cors import CORS
from flasgger import Swagger

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})

@app.teardown_appcontext
def close_db(exception):
    """Calls storage close() method"""
    storage.close()

@app.errorhandler(404)
def page_not_found(error):
    """Returns a custom 404 page not found response"""
    return make_response(jsonify({"error": "Not found"}), 404)

app.config['SWAGGER'] = {
    'title': 'AirBnB clone - RESTful API',
    'description': (
        'This is the API that was created for the HBNB RESTful API project, '
        'all the documentation will be shown below'
    ),
    'uiversion': 3
}

Swagger(app)

if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', default='0.0.0.0')
    port = getenv('HBNB_API_PORT', default=5000)
    app.run(host=host, port=int(port), threaded=True)
