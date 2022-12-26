

import sqlite3
from flask import request, Flask
import os
DATABASE = os.path.dirname(os.path.abspath(__file__)) + '\quiz-bdd.db'

app = Flask(__name__)


class BddRequete:
    def postQuestions():

        con = sqlite3.connect(DATABASE)
        data_request = request.get_json()
        position = data_request["position"]
        title = data_request["title"]
        text = data_request["text"]
        image = data_request["image"]
        data_to_insert = (position, title, text, image)
        sql_insert_query = """insert into questions (Position,Titre,Texte,Image) values(?,?,?,?)"""

        cur = con.cursor()
        cur.execute(sql_insert_query, data_to_insert)
        con.commit()
        return data_request

    def get_db():
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = sqlite3.connect(DATABASE)
        return db

    @app.teardown_appcontext
    def close_connection(exception):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()
