from django.db import models

class Task(models.Model):
    TIER = {
        (0, 'Novice'),
        (1, 'Apprentice'),
        (2, 'Adept'),
        (3, 'Expert'),
        (4, 'Master'),
        (5, 'Legendary'),
    }
    title = models.CharField(max_length=64)
    content = models.TextField()
    date = models.DateField()
    level = models.IntegerField(choices=TIER)

