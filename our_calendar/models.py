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

    def __str__(self):
        return str(self.title) + " " + str(self.date)


class Answer(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    email = models.EmailField()
    file = models.FileField(upload_to='answers/%Y/%m/%d/',blank=True)
    url = models.URLField(blank=True)
    is_checked = models.BooleanField(default=False)
    is_correct = models.BooleanField()

    class Meta:
        db_table = 'answer_key'
        constraints = [
            models.UniqueConstraint(fields=['email', 'task'], name='unique key')
        ]
