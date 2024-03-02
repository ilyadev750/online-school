from rest_framework import serializers
from users.serializers import AuthorSerializer, StudentSerializer


class ProductSerializer(serializers.Serializer):
    """Сериализатор продукта"""
    id = serializers.IntegerField(read_only=True)
    product_name = serializers.CharField(max_length=100, read_only=True)
    start_date = serializers.DateTimeField(read_only=True)
    price = serializers.IntegerField(read_only=True)
    author = AuthorSerializer(read_only=True)
    video_quantity = serializers.IntegerField(read_only=True)


class PurchaseSerializer(serializers.Serializer):
    """Сериализатор проверки статуса оплаты"""
    id = serializers.IntegerField(read_only=True)
    username = StudentSerializer(read_only=True)
    product_id = ProductSerializer(read_only=True)
    status = serializers.BooleanField(read_only=True)
