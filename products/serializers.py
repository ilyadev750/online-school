from rest_framework import serializers
from users.serializers import AuthorSerializer
from lessons.models import Lesson


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    product_name = serializers.CharField(max_length=100, read_only=True)
    start_date = serializers.DateTimeField(read_only=True)
    price = serializers.IntegerField(read_only=True)
    author = AuthorSerializer(read_only=True)
    video_quantity = serializers.IntegerField(read_only=True)