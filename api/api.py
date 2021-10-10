from flask import Flask, request, jsonify
from api.db import DBClient
import logging
import os

api = Flask(__name__)

gunicorn_logger = logging.getLogger('gunicorn.error')
api.logger.handlers.extend(gunicorn_logger.handlers)
api.logger.setLevel(gunicorn_logger.level)

db_client = DBClient('metrics-db', 'metrics', os.environ.get('DB_USER'), os.environ.get('DB_PASSWORD'))


@api.route('/orchard', methods=['POST'])
def store_orchard_data():
    json_data = request.get_json()
    if 'name' not in json_data or 'humidity' not in json_data:
        raise Exception('name or humidity fields are missing.')

    db_client.store_orchard_data(json_data['name'], json_data['humidity'])

    return '', 204


@api.errorhandler(500)
def error_handler(ex):
    return jsonify({'error': str(ex)}), 500