from rest_framework import serializers
from .models import Task, Answer


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','title','date']


class TaskFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class AnswerPostSerializer(serializers.ModelSerializer):
    task = serializers.StringRelatedField()
    class Meta:
        model = Answer
        fields = ['task','date','email','file','url']
