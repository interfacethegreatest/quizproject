from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class quizAnswer(models.Model):
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
    
class quizQuestion(models.Model):
    text = models.TextField()
    answers = models.ManyToManyField(quizAnswer, blank=False)  # Use ManyToManyField for multiple answers
    
    def __str__(self):
        return self.text

class Quiz(models.Model):
    STATUS_CHOICES = [
        ('ready', 'Ready to use'),
        ('testing', 'Needs testing'),
        ('draft', 'Draft'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    difficulty = models.CharField(max_length=20)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    questions = models.ManyToManyField(quizQuestion, blank=True)  # Use ManyToManyField for multiple questions
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    subject = models.CharField(max_length=100, default='General Knowledge')  # New field for subject
    
    class Meta:
        verbose_name_plural = 'Quizzes'

    def __str__(self):
        return self.title


