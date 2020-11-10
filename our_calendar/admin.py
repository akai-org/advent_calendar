from django.contrib import admin
from .models import Task, CorrectAnswer


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'taskDay', 'taskDate', 'level', 'category']
    list_filter = ['taskDay', 'taskDate', 'level', 'category']


@admin.register(CorrectAnswer)
class CorrectAnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'taskId']
    list_filter = ['taskId',]
