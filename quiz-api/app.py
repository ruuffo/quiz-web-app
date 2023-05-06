from flask import Flask, request
from flask_cors import CORS
from werkzeug.exceptions import Unauthorized

import db_utils
import jwt_utils

app = Flask(__name__)
CORS(app, resources={
     r"/*": {"origins": "http://localhost:3000", "supports_credentials": True}})

# app.config['CORS_HEADERS'] = 'Content-Type'


def authentification():
    auth_header = request.headers.get('Authorization')
    if auth_header is None:
        print("auth_header is None")
        return 'Unauthorized', 401

    auth_type, auth_token = auth_header.split()
    if auth_type != 'Bearer':
        print("auth_type != Bearer")
        return 'Unauthorized', 401

    try:
        jwt_utils.decode_token(auth_token)
    except Exception as e:
        print("error", e)
        return f'Unauthorized: {e}', 401


@app.route('/')
def hello_world():
    x = 'world'
    return f"Hello, {x}"


@app.route('/player/<player_name>', methods=['DELETE'])
def delete_participations(player_name: str):
    return db_utils.delete_participations(player_name=player_name)


@app.route('/player/<player_name>', methods=['GET'])
def get_player_exists(player_name: str):
    return db_utils.get_player_exists(player_name)


@app.route('/quiz-info', methods=['GET'])
def get_quiz_info():
    return db_utils.get_quiz_info()


@app.route('/questions/<int:id>', methods=['GET'])
def get_question_by_id(id: int):
    return db_utils.get_question_by_id(id)


@app.route('/questions', methods=['GET'])
def get_question_by_position():
    return db_utils.get_question_by_position(request.args.get('position'))


@app.route('/questions/<int:id>', methods=['PUT'])
def update_question(id: int):
    retour_auth = authentification()
    if retour_auth != None:
        return retour_auth
    return db_utils.update_question(id)


@app.route('/login', methods=['POST'])
def postLogin():
    payload = request.get_json()
    if (payload["password"] == 'flask2023'):
        return {'token': jwt_utils.build_token()}
    else:
        return 'Unauthorized', 401


@app.route('/questions', methods=['POST'])
def add_question():
    retour_auth = authentification()
    if retour_auth != None:
        return retour_auth
    return db_utils.add_question()


@app.route('/questions/<int:id>', methods=['DELETE'])
def delete_question(id: int):
    retour_auth = authentification()
    if retour_auth != None:
        return retour_auth
    return db_utils.delete_question(id)


@app.route('/questions/all', methods=['DELETE'])
def delete_all_questions():
    retour_auth = authentification()
    if retour_auth != None:
        return retour_auth
    return db_utils.delete_all_questions()


@app.route('/questions/all', methods=['GET'])
def get_all_questions():
    retour_auth = authentification()
    if retour_auth != None:
        return retour_auth
    return db_utils.get_all_questions()


@app.route('/participations/all', methods=['DELETE'])
def delete_all_participations():
    retour_auth = authentification()
    if retour_auth != None:
        return retour_auth
    return db_utils.delete_all_participations()


@app.route('/rebuild-db', methods=['POST'])
def rebuild_db():
    return db_utils.rebuild_db()


@app.route('/participations', methods=['POST'])
# @cross_origin(origin="http://localhost:3000")
def register_participation():
    return db_utils.register_participation()


if __name__ == "__main__":
    app.run()
