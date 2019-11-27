from django.db import models


class Task(models.Model):
    NOVICE = 'Po prostu kod'
    APPRENTICE = 'Dokumentacja i kod'
    ADEPT = 'Krew, Stack Overflow i łzy'
    EXPERT = 'Droga ku depresji'
    TIER = (
        (NOVICE, 'Po prostu kod'),
        (APPRENTICE, 'Dokumentacja i kod'),
        (ADEPT, 'Krew, Stack Overflow i łzy'),
        (EXPERT, 'Droga ku depresji'),
    )
    title = models.CharField(max_length=127)
    content = models.TextField()
    date = models.DateField()
    level = models.CharField(max_length = 31, choices=TIER)


class Answer(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    email = models.EmailField()
    file = models.FileField(upload_to='answers/%Y/%m/%d/',blank=True)
    url = models.URLField(blank=True)
    is_checked = models.BooleanField(default=False)
    is_correct = models.BooleanField()
    superkey = models.CharField(max_length=127, primary_key=True)

