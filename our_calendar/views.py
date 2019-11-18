from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TaskSerializer,TaskFullSerializer, AnswerSerializer
from rest_framework.response import Response
from .models import Task, Answer

class TaskViewset(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = TaskFullSerializer(instance)
        return Response(serializer.data)


class AnswerViewset(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
