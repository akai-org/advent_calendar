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
    title = models.CharField(max_length=64)
    content = models.TextField()
    date = models.DateField()
    level = models.CharField(max_length = 32, choices=TIER)

    def __str__(self):
        return str(self.title) + " " + str(self.date)


class Answer(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    email = models.EmailField()
    file = models.FileField(upload_to='answers/%Y/%m/%d/',blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    is_checked = models.BooleanField(default=False)
    is_correct = models.BooleanField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['email', 'task'], name='unique key')
        ]
