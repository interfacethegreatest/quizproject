from django.shortcuts import render
import requests
import json
from django.http import JsonResponse
from json import dumps
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import CatalogStringForm
from pathlib import Path
import os 
# Create your views here.
def output(request):
    data = requests.get("https://reqres.in/api/users")
    data = data.text
    return render(request, 'home.html', {'data': data})

def button(request):
    return render(request, 'home.html')

def take_tma_view(request):
    return render(request, 'takeTMA.html')

def take_module_page(request):
    return render(request, 'takeModule.html')

def get_module(module_loc):
    questionLines = load_file(module_loc)
    counter = 1
    quizQuestions = dict()
    for lines in questionLines:
        lines.rstrip()
        questionObject = lines.split('*')
        questionObject[2] = questionObject[2].split('-')
        questionObject[3] = questionObject[3].split('-')
        if questionObject[0] =='M':
            questionObject[3][-1] = questionObject[3][-1][0]
            questionObj = {
                "Type" : questionObject[0],
                "Question": questionObject[1],
                "Solutions": questionObject[2],
                "correctAnswers": questionObject[3]}
            quizQuestions[str(counter)] = questionObj
        elif questionObject[0] =='F':
            questionObject[3][-1] = questionObject[3][-1].rstrip()
            questionObj = {
                "Type" : questionObject[0],
                "Question" : questionObject[1],
                "Solutions" : questionObject[2],
                "CorrectAnswers": questionObject[3]}
            quizQuestions[str(counter)] = questionObj
        print(quizQuestions[str(counter)])
        counter+=1
    with open("requestedModule.json", "w") as write_file:
        json.dump(quizQuestions, write_file, indent=4)
    return quizQuestions



def load_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return lines
    
def get_questions_TMA(string : str):
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


def add(request):
    modules = ['05','06','07']
    result ='false'
    val1 = request.POST["num1"]
    for values in modules:
        if val1 == values:
            file ='\module'+val1+'.txt'
            path = os.getcwd()+file
            result = get_module(path)
    return render(request, 'takeModule.html', {'result':result})

def take_tma_03(request):
    file = '\TMA03.txt'
    path = os.getcwd()+file
    questions = get_questions_TMA(path)
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

