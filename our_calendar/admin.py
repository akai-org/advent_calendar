from django.contrib import admin
from .models import Task, Answer


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['date']


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['task','is_checked','is_correct','date']
    list_filter = ['task','is_checked','is_correct','date']
