# Generated by Django 5.0.1 on 2024-03-18 13:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("item2", "0007_remove_quizquestion_answers_remove_quiz_questions_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quiz",
            name="time",
            field=models.IntegerField(
                default=0, help_text="Duration of the quiz in minutes."
            ),
        ),
    ]
