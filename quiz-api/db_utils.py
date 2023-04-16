import os
import sqlite3

from flask import Flask, Response, g, request

from answer import *
from question import *

DATABASE_PATH = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'quiz-bdd.db')

app = Flask(__name__)


def connect_to_database():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.isolation_level = None
    return connection


def get_quiz_info():
    connection = connect_to_database()
    cursor = connection.cursor()

    cursor.execute('SELECT COUNT(*) FROM questions')
    nb_questions = cursor.fetchone()[0]
    cursor.execute("SELECT DISTINCT playerName FROM participations")
    participants = cursor.fetchall()
    scores = []

    for participant in participants:
        score_participant = 0
        playerName = participant[0]
        cursor.execute(
            "SELECT answers,question_position FROM participations WHERE playerName = ?", (playerName,))
        participations = cursor.fetchall()
        for participation in participations:
            answer = participation[0]
            question_position = participation[1]
            question = Question.from_json(
                get_question_by_position(question_position))
            for i in range(0, len(question.possibleAnswers)):
                if question.possibleAnswers[i]["isCorrect"] == True:
                    idx_correct_answer = i+1
                    break
            if answer == idx_correct_answer:
                score_participant += 1
        scores.append({"playerName": playerName, "score": score_participant})
    sorted_scores = sorted(scores, key=lambda x: x["score"], reverse=True)
    return {"size": nb_questions, "scores": sorted_scores}, 200


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
    sql_insert_answer = " insert into ANSWERS (question_id,is_correct,idx_answer,text) values(?,?,?,?)"
    try:

        cursor = connection.cursor()
        insertion_result = cursor.execute(
            sql_insert_question, data_to_insert_question)
        question_id = cursor.lastrowid

        possible_answers = data["possibleAnswers"]
        idx_answer = 1
        for possible_answer in possible_answers:

            ps = (question_id,
                  possible_answer["isCorrect"], idx_answer, possible_answer["text"])
            cursor.execute(
                sql_insert_answer, ps)
            idx_answer += 1
        connection.commit()
        return {'id': question_id}, 200

    except sqlite3.Error as e:
        connection.rollback()
        return Response(f"An error occurred: {e}", status=500)


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
    question = Question(_id=question_data[0], title=question_data[1], text=question_data[2],
                        position=question_data[4], image=question_data[3], possibleAnswers=[])
    for answer_data in answers_data:

        answer = {"text": answer_data[4], "isCorrect": (answer_data[2] != 0)}
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
    question = Question(_id=question_data[0], title=question_data[1], text=question_data[2],
                        position=question_data[4], image=question_data[3], possibleAnswers=[])
    for answer_data in answers_data:
        answer = {"text": answer_data[4], "isCorrect": (answer_data[2] != 0)}
        question.possibleAnswers.append(answer)
    # Retourner la question sous forme de dictionnaire

    return question.to_json()


# def set_question_at_position(id: int):

#     connection = connect_to_database()
#     cursor = connection.cursor()
#  # Récupérer les données de la requête
#     data = request.get_json()

#     new_position=data["position"]

#     # Si la nouvelle position est inférieure à la position actuelle, décaler les questions entre la nouvelle position et la position actuelle d'une position vers le bas
#     if new_position < current_position:
#         cursor.execute(
#             "UPDATE questions SET position = position + 1 WHERE position >= ? AND position < ?", (new_position, current_position))
#     # Si la nouvelle position est supérieure à la position actuelle, décaler les questions entre la position actuelle et la nouvelle position d'une position vers le haut
#     elif new_position > current_position:
#         cursor.execute(
#             "UPDATE questions SET position = position - 1 WHERE position > ? AND position <= ?", (current_position, new_position))
#     connection.commit()

#     # Mettre à jour la position de la question
#     cursor.execute(
#         "UPDATE questions SET position=? WHERE id=?", (new_position, id))
#     connection.commit()

#     # Retourner un code de réussite
#     return Response(status=200)


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
            "CREATE TABLE answers (id INTEGER PRIMARY KEY AUTOINCREMENT, question_id INTEGER, is_correct INTEGER,idx_answer INTEGER, text TEXT)")
      # Drop 'participations' table if it exists
        cursor.execute("DROP TABLE IF EXISTS participations")

    # Create 'participations' table
        cursor.execute(
            "CREATE TABLE participations (id INTEGER PRIMARY KEY AUTOINCREMENT,question_position INTEGER, playerName TEXT, answers INTEGER)")
        connection.commit()
        connection.close()
        return Response("Ok", status=200)
    except sqlite3.Error as e:
        return Response(f"An error occurred: {e}", status=500)


def register_participation():
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        nb_questions = get_quiz_info()[0]["size"]

        data = request.get_json()
        if len(data["answers"]) != nb_questions:
            return Response(response='The number of question is incorrect', status=400)

        for i in range(0, len(data["answers"])):

            cursor.execute(
                "INSERT INTO participations (playerName,answers,question_position) VALUES (?,?,?)", (data["playerName"], data["answers"][i], i+1))

        scores = get_quiz_info()[0]['scores']
        for player in scores:
            if player["playerName"] == data["playerName"]:
                score_participant = player['score']
                break
        return {"score": score_participant, "playerName": data["playerName"]}, 200

    except sqlite3.Error as e:
        return Response(f"An error occurred: {e}", status=500)


def delete_all_questions():
    connection = connect_to_database()
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM answers")
        cursor.execute("DELETE FROM questions")
        cursor.execute(
            "UPDATE sqlite_sequence SET seq = 0 WHERE name = 'questions'")
        cursor.execute(
            "UPDATE sqlite_sequence SET seq = 0 WHERE name = 'answers'")
        connection.commit()
        return Response(status="204", response="All questions have been deleted succesfully.")
    except sqlite3.Error as e:
        return Response(status="200", response=f"An error occurred: {e}")


def update_question(id: int):
    question_json = get_question_by_id(id)

    # Si la question n'a pas été trouvée, retourner une erreur 404
    if not isinstance(question_json, str):
        return Response(response=f'Question with id "{id}" does not exists', status=404)

    question = Question.from_json(question_json)
    connection = connect_to_database()
    cursor = connection.cursor()

    # Récupérer les données de la requête
    data = request.get_json()
    current_position = question.position
    new_position = data["position"]

    #  Si la nouvelle position est inférieure à la position actuelle, décaler les questions entre la nouvelle position et la position actuelle d'une position vers le bas
    if new_position < current_position:
        cursor.execute(
            "UPDATE questions SET position = position + 1 WHERE position >= ? AND position < ?", (new_position, current_position))
    # Si la nouvelle position est supérieure à la position actuelle, décaler les questions entre la position actuelle et la nouvelle position d'une position vers le haut
    elif new_position > current_position:
        cursor.execute(
            "UPDATE questions SET position = position - 1 WHERE position > ? AND position <= ?", (current_position, new_position))
    # connection.commit()
    # Mettre à jour les données de la question dans la base de données
    cursor.execute("UPDATE questions SET title=?, text=?, image=?, position=? WHERE id=?",
                   (data["title"], data["text"], data["image"], data["position"], id))

    # connection.commit()

    # Mettre à jour les réponses associées à la question
    cursor.execute("DELETE FROM answers WHERE question_id=?", (id,))
    possible_answers = data["possibleAnswers"]
    idx_answer = 1
    for possible_answer in possible_answers:
        cursor.execute("INSERT INTO answers (question_id, is_correct,idx_answer, text) VALUES (?, ?, ?,?)",
                       (id, possible_answer["isCorrect"], idx_answer, possible_answer["text"]))
        idx_answer += 1
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
    question_json = get_question_by_id(id)

    # Si la question n'a pas été trouvée, retourner une erreur 404
    if not isinstance(question_json, str):
        return Response(response=f'Question with id "{id}" does not exists', status=404)

    question = Question.from_json(question_json)

    connection = connect_to_database()
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM questions WHERE id=?", (id,))
        if cursor.rowcount == 0:
            return Response(response=f'Question with id "{id}" does not exists', status=404)
        cursor.execute("DELETE FROM answers WHERE question_id=?", (id,))
        cursor.execute(
            "UPDATE questions SET position = position - 1 WHERE position > ? ", (question.position,))

        connection.commit()
        return Response(response='Question deleted successfully', status=204)
    except sqlite3.Error as e:

        return Response(response=f"An error occurred: {e}", status=500)


def get_all_questions():
    connection = connect_to_database()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT position,title FROM questions")
        questions_data = cursor.fetchall()
        questions_list = []
        for row in questions_data:
            question = {"title": row[1],"position":row[0]}
            questions_list.append(question)
        return {"listAllQuestions": questions_list}, 200
    except sqlite3.Error as e:
        return {f"An error occurred: {e}", 500}


@app.teardown_appcontext
def close_connection(exception):
    connection = getattr(g, '_database', None)
    if connection is not None:
        connection.close()
