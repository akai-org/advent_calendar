from rest_framework import serializers
from .models import Task, UserAnswer


class TaskFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class UserAnswerPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = '__all__'
