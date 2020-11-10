from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
import datetime

from .models import Task, CorrectAnswer
from .serializers import TaskFullSerializer, UserAnswerPostSerializer


def DayTodayViewset(request):
    nowIs=datetime.datetime.now()
    jsonNowIS = {"today": nowIs.strftime("%Y-%m-%d")}
    return JsonResponse(jsonNowIS)


class TaskViewset(viewsets.ModelViewSet):
    serializer_class = TaskFullSerializer
    queryset = Task.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['taskDate', ]
    ordering = ('taskDate',)


class ToTodayTaskViewset(viewsets.ModelViewSet):
    serializer_class = TaskFullSerializer
    queryset = Task.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['taskDate', ]
    ordering = ('taskDate',)

    def get_queryset(self):
        nowIs_forTasks = datetime.datetime.now()
        tasks = Task.objects.filter(taskDate__lte = nowIs_forTasks.strftime("%Y-%m-%d"))
        return tasks


@api_view(['POST'])
def PostAnswerViewset(request):

    if request.method == 'POST':
        serializer = UserAnswerPostSerializer(data=request.data)
        if serializer.is_valid():
            value = serializer.data['userAnswer'] == CorrectAnswer.objects.get(taskId=serializer.data['taskId']).correctAnswer
            return Response(value, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
