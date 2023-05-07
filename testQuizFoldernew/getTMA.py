from flask import Flask, jsonify
import random

app = Flask(__name__)

def load_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return lines
    
def get_questions():
    questionLines = load_file('questions.txt')
    random.shuffle(questionLines)
    questions = []
    for lines in questionLines:
        lines.strip('\n')
        questionObject = lines.split(',')
        answers = questionObject[1]
        answers = answers.split('-')
        questionObject[1] = answers 
        questions.append(questionObject)
    return questions

@app.route('/generate_quiz_questions')
def generate_quiz_questions():
    questions = get_questions()
    quizQuestions = []
    for question in questions:
        random.shuffle(question[1])
        questionObj = {
            "question": question[0],
            "answers": question[1],
            "correctAnswer": question[2]
        }
        quizQuestions.append(questionObj)
    return jsonify(quizQuestions)

if __name__ == '__main__':
    app.run(debug=True)
