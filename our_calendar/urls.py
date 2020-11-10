from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from .views import TaskViewset, PostAnswerViewset, DayTodayViewset, ToTodayTaskViewset


router = routers.DefaultRouter()
router.register(r'tasks/all', TaskViewset),
router.register(r'tasks/now', ToTodayTaskViewset)


urlpatterns = [
    url(r'^', include(router.urls)),
    path('tasks/answer', PostAnswerViewset, name="create"),
    path('today/', DayTodayViewset)
]
