import sqlite3
from flask import request, Flask, g
import os
from question import *

DATABASE_PATH = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'quiz-bdd.db')

app = Flask(__name__)


def connect_to_database():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.isolation_level = None
    return connection


def add_question():
    connection = connect_to_database()
    cursor = connection.cursor()

    data = request.get_json()

    data_to_insert_question = (
        data["title"], data["text"], data["image"], data["position"])

    sql_insert_question = "insert into questions (title,text,position,image) values(?,?,?,?)"
    sql_insert_answer = " insert into ANSWERS (question_id,is_correct,text) values(?,?,?)"
    try:

        cursor = connection.cursor()
        insertion_result = cursor.execute(
            sql_insert_question, data_to_insert_question)
        question_id = cursor.lastrowid

        possible_answers = data["possibleAnswers"]
        for possible_answer in possible_answers:
       
            ps = (question_id,
                  possible_answer["isCorrect"], possible_answer["text"])
            cursor.execute(
                sql_insert_answer, ps)
        connection.commit()
        return insertion_result

    except sqlite3.Error as e:

        print(f"An error occurred: {e}")
        connection.rollback()
        return None



def delete_all_questions():
    connection = connect_to_database()

    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM questions")
        connection.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


def delete_question():
    connection = connect_to_database()
    data_request = request.get_json()
    question_id = data_request["ID"]
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM questions WHERE id=?", (question_id,))
        connection.commit()
        return True
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return False


@app.teardown_appcontext
def close_connection(exception):
    connection = getattr(g, '_database', None)
    if connection is not None:
        connection.close()
