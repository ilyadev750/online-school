from rest_framework import serializers
from .models import Author, Student


class AuthorSerializer(serializers.ModelSerializer):
    """Сериализатор автора/преподавателя продукта"""
    class Meta:
        model = Author
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    """Сериализатор студента"""
    class Meta:
        model = Student
        fields = '__all__'
