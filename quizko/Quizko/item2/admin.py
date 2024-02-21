from django.contrib import admin
from.models import quizAnswer, quizQuestion,Quiz
# Register your models here.
admin.site.register(quizAnswer)
admin.site.register(quizQuestion)
admin.site.register(Quiz)