from django.db import models
from django.utils.timezone import now


class Task(models.Model):
    NOVICE = 'Po prostu kod'
    APPRENTICE = 'Dokumentacja i kod'
    ADEPT = 'Dokumentacja, Stack Overflow i łzy'
    EXPERT = 'Droga ku depresji'
    TIER = (
        (NOVICE, 'Po prostu kod'),
        (APPRENTICE, 'Dokumentacja i kod'),
        (ADEPT, 'Dokumentacja, Stack Overflow i łzy'),
        (EXPERT, 'Droga ku depresji'),
    )
    taskDay = models.IntegerField("day of task", default=0)
    taskDate = models.DateField("date of task", default=now)
    level = models.CharField(max_length=64, choices=TIER, default=NOVICE)
    taskContent = models.TextField(default="Some good stuff for user")
    category = models.CharField(max_length=64, default="JavaScript")

    def __str__(self):
        return str(self.taskDate)


class CorrectAnswer(models.Model):
    taskId = models.OneToOneField(Task, to_field='id', on_delete=models.CASCADE)
    correctAnswer = models.TextField(default="Some good stuff")


class UserAnswer(models.Model):
    taskId = models.ForeignKey(Task, to_field='id', on_delete=models.CASCADE)
    userAnswer = models.TextField(default="None")
    date = models.DateField(auto_now_add=True)
