import sqlite3
from flask import request, Flask, g, Response
import os
from question import *
from answer import *

DATABASE_PATH = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'quiz-bdd.db')

app = Flask(__name__)


def connect_to_database():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.isolation_level = None
    return connection


def position_reordering(position: int):
    connection = connect_to_database()
    cursor = connection.cursor()

    # Récupérer toutes les questions avec une position supérieure ou égale à la position donnée
    cursor.execute("SELECT * FROM questions WHERE position >= ?", (position,))
    questions_data = cursor.fetchall()

    # Mettre à jour les positions de ces questions
    for question_data in questions_data:
        question_id = question_data[0]
        new_position = question_data[4] + 1
        cursor.execute("UPDATE questions SET position=? WHERE id=?",
                       (new_position, question_id))
    connection.commit()


def add_question():
    connection = connect_to_database()
    cursor = connection.cursor()

    data = request.get_json()
    position_reordering(data["position"])
    data_to_insert_question = (
        data["title"], data["text"], data["image"], data["position"])

    sql_insert_question = "insert into questions (title,text,image,position) values(?,?,?,?)"
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
        return {'id': question_id}

    except sqlite3.Error as e:

        print(f"An error occurred: {e}")
        connection.rollback()
        return None


def get_question_by_position(position: int):
    connection = connect_to_database()
    cursor = connection.cursor()

    # Récupérer la question avec l'identifiant donné
    cursor.execute("SELECT * FROM questions WHERE position=?", (position,))
    question_data = cursor.fetchone()
    # Si la question n'a pas été trouvée, retourner une erreur 404
    if question_data is None:
        return Response(response=f'Question with position "{position}" does not exists', status=404)

    # Récupérer les réponses associées à la question
    question_id = question_data[0]
    cursor.execute("SELECT * FROM answers WHERE question_id=?", (question_id,))
    answers_data = cursor.fetchall()

    # Construire l'objet Question à partir des données de la base de données
    question = Question(title=question_data[1], text=question_data[2],
                        position=question_data[4], image=question_data[3], possibleAnswers=[])
    for answer_data in answers_data:
        answer = {"text": answer_data[3], "isCorrect": (answer_data[2] != 0)}
        question.possibleAnswers.append(answer)
    # Retourner la question sous forme de dictionnaire

    return question.to_json()


def get_question_by_id(id: int):
    connection = connect_to_database()
    cursor = connection.cursor()

    # Récupérer la question avec l'identifiant donné
    cursor.execute("SELECT * FROM questions WHERE id=?", (id,))
    question_data = cursor.fetchone()

    # Si la question n'a pas été trouvée, retourner une erreur 404
    if question_data is None:
        return Response(response=f'Question with id "{id}" does not exists', status=404)

    # Récupérer les réponses associées à la question
    cursor.execute("SELECT * FROM answers WHERE question_id=?", (id,))
    answers_data = cursor.fetchall()

    # Construire l'objet Question à partir des données de la base de données
    question = Question(title=question_data[1], text=question_data[2],
                        position=question_data[4], image=question_data[3], possibleAnswers=[])
    for answer_data in answers_data:
        answer = {"text": answer_data[3], "isCorrect": (answer_data[2] != 0)}
        question.possibleAnswers.append(answer)
    # Retourner la question sous forme de dictionnaire

    return question.to_json()


def set_question_at_position(current_position: int):

    connection = connect_to_database()
    cursor = connection.cursor()
 # Récupérer les données de la requête
    data = request.get_json()

    new_position=data["position"]

    # Si la nouvelle position est inférieure à la position actuelle, décaler les questions entre la nouvelle position et la position actuelle d'une position vers le bas
    if new_position < current_position:
        cursor.execute(
            "UPDATE questions SET position = position + 1 WHERE position >= ? AND position < ?", (new_position, current_position))
    # Si la nouvelle position est supérieure à la position actuelle, décaler les questions entre la position actuelle et la nouvelle position d'une position vers le haut
    elif new_position > current_position:
        cursor.execute(
            "UPDATE questions SET position = position - 1 WHERE position > ? AND position <= ?", (current_position, new_position))
    connection.commit()

    # Mettre à jour la position de la question
    cursor.execute(
        "UPDATE questions SET position=? WHERE position=?", (new_position, current_position))
    connection.commit()

    # Retourner un code de réussite
    return Response(status=200)


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
      # Drop 'participations' table if it exists
        cursor.execute("DROP TABLE IF EXISTS participations")

    # Create 'participations' table
        cursor.execute(
            "CREATE TABLE participations (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, question_id INTEGER, answer_id INTEGER)")
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
        return Response(status="204", response="All questions have been deleted succesfully.")
    except sqlite3.Error as e:
        return Response(status="200", response=f"An error occurred: {e}")


def update_question(id: int):
    connection = connect_to_database()
    cursor = connection.cursor()

    # Récupérer la question avec l'identifiant donné
    cursor.execute("SELECT * FROM questions WHERE id=?", (id,))
    question_data = cursor.fetchone()

    # Si la question n'a pas été trouvée, retourner une erreur 404
    if question_data is None:
        return Response(response=f'Question with id "{id}" does not exists', status=404)

    # Récupérer les données de la requête
    data = request.get_json()

    # Mettre à jour les données de la question dans la base de données
    cursor.execute("UPDATE questions SET title=?, text=?, image=?, position=? WHERE id=?",
                   (data["title"], data["text"], data["image"], data["position"], id))
    connection.commit()

    # Mettre à jour les réponses associées à la question
    cursor.execute("DELETE FROM answers WHERE question_id=?", (id,))
    possible_answers = data["possibleAnswers"]
    for possible_answer in possible_answers:
        cursor.execute("INSERT INTO answers (question_id, is_correct, text) VALUES (?, ?, ?)",
                       (id, possible_answer["isCorrect"], possible_answer["text"]))
    connection.commit()

    # Retourner un code de réussite
    return Response(status=204)


def delete_all_participations():
    connection = connect_to_database()
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM participations")
        connection.commit()
        return Response(status="204", response="All participations have been deleted succesfully.")
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
        return Response(response='Question deleted successfully', status=204)
    except sqlite3.Error as e:

        return Response(response=f"An error occurred: {e}", status=500)


@app.teardown_appcontext
def close_connection(exception):
    connection = getattr(g, '_database', None)
    if connection is not None:
        connection.close()
