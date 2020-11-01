from rest_framework import serializers
from .models import Task, Answer


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','title','date','level']


class TaskFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class AnswerPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['task','email','file','url','date','is_checked','is_correct','superkey']
