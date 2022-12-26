from flask import Flask, request, g
from flask_cors import CORS
import jwt
from bddrequete import BddRequete
import datetime
from werkzeug.exceptions import Unauthorized


app = Flask(__name__)
CORS(app)


class JwtError(Exception):
    """Exception raised for jwt errors in the quiz app
    """

    def __init__(self, message="Jwt error"):
        self.message = message
        super().__init__(self.message)


secret = "Super secret key know one will ever know, right ?"
expiration_in_seconds = 3600


def build_token():
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=expiration_in_seconds),
            'iat': datetime.datetime.utcnow(),
            'sub': 'quiz-app-admin'
        }
        return jwt.encode(
            payload,
            secret,
            algorithm="HS256"
        )
    except Exception as e:
        return e


def decode_token(auth_token):
    """
    Decodes the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
        payload = jwt.decode(auth_token, secret, algorithms="HS256")
        # if decoding did not fail, this means we are correctly logged in
        return payload['sub']
    except jwt.ExpiredSignatureError:
        raise JwtError('Signature expired. Please log in again.')
    except jwt.InvalidTokenError as e:
        raise JwtError('Invalid token. Please log in again.')


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
        return build_token()
    else:
        return 'Unauthorized', 401


@app.route('/questions', methods=['POST'])
def endpointQuestion():
    return BddRequete.postQuestions()


if __name__ == "__main__":
    app.run()
