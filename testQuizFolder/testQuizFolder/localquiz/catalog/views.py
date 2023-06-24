from django.shortcuts import render
import requests
import json
from django.http import JsonResponse

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

def take_tma_03(request):
    questionLines = load_file('/home/kali/Documents/quizproject-main/testQuizFolder/TMA03.txt')
    questions = []
    for lines in questionLines:
        lines.strip('\n')
        questionObject = lines.split(',')
        answers = questionObject[1]
        answers = answers.split('-')
        questionObject[1] = answers 
        questions.append(questionObject)
    data = json.dumps(questions)
    context = {'json_data':json_data}
    return render(request, 'takeTMA.html', context)


#def TakeModuleTest(request):
#    return render(request, ' ')