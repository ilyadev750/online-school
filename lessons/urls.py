from django.urls import path
from .views import LessonSet


urlpatterns = [
    path('lessons/', LessonSet.as_view(), name='lessons'),
]
