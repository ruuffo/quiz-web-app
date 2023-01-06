import sqlite3
from flask import request, Flask, g, Response
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


def rebuild_db():
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        # Drop 'questions' table if it exists
        cursor.execute("DROP TABLE IF EXISTS questions")

        # Create 'questions' table
        cursor.execute(
            "CREATE TABLE questions (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, text TEXT, image TEXT, position INTEGER)")

        # Drop 'answers' table if it exists
        cursor.execute("DROP TABLE IF EXISTS answers")

        # Create 'answers' table
        cursor.execute(
            "CREATE TABLE answers (id INTEGER PRIMARY KEY AUTOINCREMENT, question_id INTEGER, is_correct INTEGER, text TEXT)")

        connection.commit()
        connection.close()
        return Response("Ok", status=200)
    except sqlite3.Error as e:
        return Response(f"An error occurred: {e}", status=500)


def delete_all_questions():
    connection = connect_to_database()
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM questions")
        connection.commit()
        return Response(status="200", response="All questions have been deleted succesfully.")
    except sqlite3.Error as e:
        return Response(status="200", response=f"An error occurred: {e}")


def delete_question(id: int):
    connection = connect_to_database()
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM questions WHERE id=?", (id,))
        if cursor.rowcount == 0:
            return Response(response=f'Question with id "{id}" does not exists', status=404)
        connection.commit()
        return Response(response='Question deleted successfully', status=200)
    except sqlite3.Error as e:

        return Response(response=f"An error occurred: {e}", status=500)


@app.teardown_appcontext
def close_connection(exception):
    connection = getattr(g, '_database', None)
    if connection is not None:
        connection.close()
