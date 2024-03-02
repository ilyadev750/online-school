from products.models import Purchase
from .models import Lesson
from rest_framework.views import APIView
from .serializers import LessonSerializer
from rest_framework.response import Response


class LessonSet(APIView):
    """Извлечение из GET запроса никнейма студента,
    проверка статуса оплаты, по ключу продукта поиск
    списка уроков и вывод ответа в JSON-формате"""
    def get(self, request, format=None):
        username = request.GET.get('username')
        purchased_products = (Purchase.objects.select_related('username')
                              .select_related('product_id')
                              .filter(username__username=username, status=True)
                              .values('product_id'))
        values = []
        for value in purchased_products:
            values.append(value['product_id'])
        lessons = (Lesson.objects.prefetch_related('product_id')
                   .filter(product_id__in=values))
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)
