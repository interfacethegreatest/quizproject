from django.shortcuts import render
import requests
import json
from django.http import JsonResponse
from django.http import HttpResponse
from json import dumps
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import CatalogStringForm
from pathlib import Path
import os 
from .models import question
import platform
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
    

def take_module_question(request):
 ifFinished = 'Thank you for taking the test!'
 dest1 = question()
 if platform.system() == 'Linux':
    module = '/module'
 else:
    module = '\module'
 file = module+get_module_number()+'.txt'
 path = os.getcwd()+file
 question_no = get_moduleQuiz_question_number()
 res = get_module(path)
 totalQuestionNo = get_no_of_test_questions()
 if question_no > totalQuestionNo:
    dest2 = ifFinished
    return render(request, 'finished.html', {'dest2' : dest2})
 res = res[str(question_no)]
 print(res)
 increment_test_question()
 dest1.module_number = get_module_number()
 question_count = str(question_no) + '/'+ str(totalQuestionNo)
 dest2 = (res, get_module_number(), question_count )
 return render(request, 'testModule.html/', {'dest2' : dest2 })


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
                "correctAnswers": questionObject[3]}
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
           new_test(val1)
           ''' file ='\module'+val1+'.txt'
            path = os.getcwd()+file
            res = get_module(path)'''
          
    return render(request, 'testModule.html')

def get_module_number():
    text_file = load_file('note.txt')
    details = text_file[0]
    details = details.split(',')
    return details[2]

def increment_test_question():
    path = 'note.txt'
    text_file = load_file(path)
    test_details = text_file[0]
    test_details = test_details.split(',')
    test_details[0] = str(1+int(test_details[0]))
    write_text = test_details[0] + ','+ test_details[1]+','+ test_details[2]+ ','+test_details[3]
    with open('note.txt', 'w') as f:
        f.write(write_text)
    

def get_moduleQuiz_mark():
    text_file = load_file('note.txt')
    details = text_file[0]
    details = details.split(',')
    return int(details[1])

def get_moduleQuiz_question_number():
    text_file = load_file('note.txt')
    details = text_file[0]
    details = details.split(',')
    return int(details[0])

def increment_correct_answers():
    text_file = load_file('note.txt')
    test_details = text_file[0]
    test_details = test_details.split(',')
    test_details[1] = str(1+int(test_details[1]))
    write_text = test_details[0] + ','+ test_details[1] + ',' + test_details[2]+','+test_details[3]
    with open('note.txt', 'w') as f:
        f.write(write_text)

def get_no_of_test_questions():
    file ='/module'+get_module_number()+'.txt'
    path = os.getcwd()+file
    with open(path) as f:
        return len(f.readlines())


def new_test(module):
    no_of_lines = get_no_of_test_questions()
    write_text = '1' + ','+ '0' + ',' + module +','+ str(no_of_lines)
    with open('note.txt', 'w') as f:
        f.write(write_text)
    



def take_tma_03(request):
    if platform.system() == 'Linux':
        file = '/TMA03.txt'
    else:
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

