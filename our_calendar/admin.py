from django.contrib import admin
from .models import Task, Answer


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['date']


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['task','date', 'email','is_checked','is_correct']
    list_filter = ['task','is_checked','is_correct','date']
