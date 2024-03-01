from django.urls import path, include
from .views import index, ProductSet
from rest_framework import routers


urlpatterns = [
    path("", index, name='home'),
    path('all_products/', ProductSet.as_view(), name='all_products'),
]
