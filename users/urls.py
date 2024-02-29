from django.urls import path
from .views import add_student_to_product

urlpatterns = [
    path("add_student/", add_student_to_product, name='add_student'),
]
