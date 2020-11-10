from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from .views import TaskViewset, OneTaskViewset, PostAnswerViewset, DayTodayViewset, ToTodayTaskViewset, OneToTodayTaskViewset


# router = routers.DefaultRouter()

urlpatterns = [
    # url(r'^', include(router.urls)),
    path('tasks/answer', PostAnswerViewset, name="create"),
    path('tasks/all/', TaskViewset),
    path('tasks/all/<id>/', OneTaskViewset, name="detail"),
    path('tasks/now/', ToTodayTaskViewset),
    path('tasks/now/<id>/', OneToTodayTaskViewset, name="detail"),
    path('today/', DayTodayViewset)
]
