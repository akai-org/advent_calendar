from rest_framework import viewsets
from .serializers import TaskSerializer,TaskFullSerializer, AnswerPostSerializer
from rest_framework.response import Response
from .models import Task, Answer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view

class TaskViewset(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = TaskFullSerializer(instance)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def answer_list(request):

    if request.method == 'POST':
        serializer = AnswerPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





