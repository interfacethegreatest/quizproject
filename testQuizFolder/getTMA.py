import json
import random
from pathlib import Path
import os

def load_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return lines

def get_module_questions(txtFileLoc:str()):
    questionLines = load_file('C:/Users/esing/Downloads/quizproject-main/quizproject-main/quizproject-main/testQuizFolder/module05.txt')
    counter = 1
    quizQuestions = dict()
    for lines in questionLines:
        lines.rstrip()
        questionObject = lines.split('*')
        questionObject[2] = questionObject[2].split('-')
        questionObject[3].rstrip()
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
    questions = json.dumps(quizQuestions)
    return questions


def get_questions():
    questionLines = load_file('questions.txt')
    questions = []
    for lines in questionLines:
        lines.strip('\n')
        questionObject = lines.split(',')
        answers = questionObject[1]
        answers = answers.split('-')
        questionObject[1] = answers 
        questions.append(questionObject)
    return questions


if __name__ == '__main__':
    print(get_module_questions('12'))
            
    



''' 12/06/2023
def get_module_questions(txtFileLoc:str()):
    questionLines = load_file('/home/kali/Documents/quizproject-main/testQuizFolder/module06.txt')
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
    return quizQuestions
'''