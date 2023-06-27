from django.shortcuts import render
import requests
import json
from django.http import JsonResponse
from json import dumps

# Create your views here.
def output(request):
    data = requests.get("https://reqres.in/api/users")
    data = data.text
    return render(request, 'home.html', {'data': data})

def button(request):
    return render(request, 'home.html')

def take_tma_view(request):
    return render(request, 'takeTMA.html')


def load_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return lines
    
def get_questions(string : str):
    questionLines = load_file(string)
    questions = []
    for lines in questionLines:
        lines.strip('\n')
        questionObject = lines.split(',')
        answers = questionObject[1]
        answers = answers.split('-')
        questionObject[1] = answers 
        questions.append(questionObject)
    return questions


def take_tma_03(request):
    questions = get_questions('/home/kali/Documents/quizproject-main/testQuizFolder/TMA03.txt')
    quizQuestions = dict()
    counter = 1
    for question in questions:
        questionObj = { 
            "question": question[0],
            "solutions": question[1],
            "correctAnswer": question[2][0]
        }
        quizQuestions[str(counter)] = questionObj
        counter += 1

    response  = quizQuestions
    return render(request, 'takeTMA.html', {'data' : quizQuestions})

