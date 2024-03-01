from django.urls import path
from .views import LessonSet


urlpatterns = [
    path('product/', LessonSet.as_view(), name='product'),
]