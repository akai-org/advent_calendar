from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
import datetime

from .models import Task, CorrectAnswer
from .serializers import TaskFullSerializer, UserAnswerPostSerializer


@api_view(['GET'])
def DayTodayViewset(request):
    if request.method == 'GET':
        nowIs=datetime.datetime.now()
        jsonNowIS = {"today": nowIs.strftime("%Y-%m-%d")}
        return JsonResponse(jsonNowIS)


@api_view(['GET'])
def TaskViewset(request):
    if request.method == 'GET':
        queryset = sorted(Task.objects.all(), key=lambda x: x.taskDay)
        serializer_class = TaskFullSerializer(queryset, many=True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def OneTaskViewset(request, id):
    try:
        queryset = Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        queryset = Task.objects.get(id=id)
        serializer_class = TaskFullSerializer(queryset)
        return Response(serializer_class.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def ToTodayTaskViewset(request):
    if request.method == 'GET':
        nowIs_forTasks = datetime.datetime.now()
        queryset = sorted(Task.objects.filter(taskDate__lte=nowIs_forTasks.strftime("%Y-%m-%d")), key=lambda x: x.taskDay)
        serializer_class = TaskFullSerializer(queryset, many=True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def OneToTodayTaskViewset(request, id):
    try:
        queryset = Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        nowIs_forTasks = datetime.datetime.now()
        if Task.objects.get(id=id).taskDate.strftime("%d") >= nowIs_forTasks.strftime("%d"):
            queryset = Task.objects.get(id=id)
            serializer_class = TaskFullSerializer(queryset)
            return Response(serializer_class.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def PostAnswerViewset(request):
    if request.method == 'POST':
        serializer = UserAnswerPostSerializer(data=request.data)
        if serializer.is_valid():
            value = serializer.data['userAnswer'] == CorrectAnswer.objects.get(taskId=serializer.data['taskId']).correctAnswer
            return Response(value, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
