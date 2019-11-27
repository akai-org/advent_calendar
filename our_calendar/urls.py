from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from .views import TaskViewset, answer_list


router = routers.DefaultRouter()
router.register(r'tasks', TaskViewset)


urlpatterns = [
    url(r'^', include(router.urls)),
    path('answer', answer_list, name="create")
]
