from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/')
def hello_world():
	x = 'maman'
	return f"Hello, {x}"

if __name__ == "__main__":
    app.run()


@app.route('/quiz-info',methods=['GET'])
def GetQuizInfo():
    return {"size":0,"scores": []}, 200
