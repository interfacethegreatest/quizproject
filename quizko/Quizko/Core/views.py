from django.shortcuts import render
from item2.models import quizAnswer,quizQuestion,Quiz
# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')


def aboutus(request):
    return render(request, 'core/aboutus.html')

def generate(request):
    return render(request, 'core/generate.html')

def browse(request):
    quizzes = Quiz.objects.all()[0:6]
    return render(request, 'core/browse.html', {
        'quizzes': quizzes
    })