from django.db import models
from django.urls import reverse
# Create your models here.

class question:
    module_number: str
    question_number: int
    question_type: str
    question_title : str
    question_text : str
    correct_answers: list
    
    