from rest_framework import serializers
from products.serializers import ProductSerializer


class LessonSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    lesson_name = serializers.CharField(max_length=100, read_only=True)
    product_id = ProductSerializer(read_only=True)
    video_link = serializers.CharField(max_length=100, read_only=True)