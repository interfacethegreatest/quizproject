from django.shortcuts import render, get_object_or_404
import json
from .models import Quiz,quizAnswer,quizQuestion

def detail(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    questions = quiz.questions.all()
    
    question_answers = {}  # Dictionary to store question texts and their associated answer texts
    
    for question in questions:
        # Retrieve all answers associated with the current question
        answers = question.answers.all()
        # Extract the answer texts and their is_correct values for the current question
        answer_texts = [{'text': answer.text, 'is_correct': answer.is_correct} for answer in answers]
        # Store the question text and its associated answer texts in the dictionary
        question_answers[question.text] = answer_texts
    
    # Serialize the question_answers dictionary into a JSON string
    question_answers_json = json.dumps(question_answers)
    
    # Write the JSON string into a file
    #with open('question_answers.json', 'w') as json_file:
     #   json_file.write(question_answers_json)
    
    return render(request, 'quiz/detail.html', {
        'quiz': quiz,
        'questions': questions,
        'question_answers_json': question_answers_json,
    })