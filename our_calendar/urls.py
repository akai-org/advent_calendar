from django.conf.urls import url, include
from rest_framework import routers
from .views import TaskViewset, AnswerViewset


router = routers.DefaultRouter()
router.register(r'tasks', TaskViewset)
router.register(r'answers', AnswerViewset)


urlpatterns = [
    url(r'^', include(router.urls))
]
