from flask import Flask, request, g
from flask_cors import CORS
import jwt_utils
import db_utils

from werkzeug.exceptions import Unauthorized


app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():

    x = 'world'
    return f"Hello, {x}"


@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
    return {"size": 0, "scores": []}, 200


@app.route('/login', methods=['POST'])
def postLogin():
    payload = request.get_json()
    if (payload["password"] == 'flask2023'):
        return {'token': jwt_utils.build_token()}
    else:
        return 'Unauthorized', 401


@app.route('/questions', methods=['POST'])
def add_question():


    auth_header = request.headers.get('Authorization')
    if auth_header is None:
        return 'Unauthorized', 401

    auth_type, auth_token = auth_header.split()
    if auth_type != 'Bearer':
        return 'Unauthorized', 401

    try:
        jwt_utils.decode_token(auth_token)
    except jwt_utils.TokenError:
        return 'Unauthorized', 401

    # If the client is authenticated, proceed with adding the question to the database
    return db_utils.add_question()


@app.route('/questions/<int:id>', methods=['DELETE'])
def delete_question(id : int):
    return db_utils.delete_question(id)


@app.route('/questions/all', methods=['DELETE'])
def delete_all_questions():
    return db_utils.delete_all_questions()

@app.route('/rebuild-db', methods=['POST'])
def rebuild_db():
    return db_utils.rebuild_db()

if __name__ == "__main__":
    app.run()
