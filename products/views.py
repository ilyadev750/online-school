from django.shortcuts import render
from .models import Product
from users.models import Student
from .serializers import ProductSerializer
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response


class ProductSet(APIView):
    """Получить список доступных продуктов в
    JSON-формате. В комментариях пример подзапроса
    расчета количества уроков в продукте. Не использовал
    в проекте из-за N+1 проблемы"""
    def get(self, request, format=None):
        # queryset = (Product.objects.select_related('author').all()
        #             .annotate(video_quantity=Subquery(
        #                 Lesson.objects.select_related('product_id')
        #                 .filter(product_id__pk=OuterRef('pk'))
        #                 .values('product_id')
        #                 .annotate(count=Count('id'))
        #                 .values('count'))))
        queryset = Product.objects.select_related('author').all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


def index(request):
    """Получить список продуктов, ссылки на добавление
    студентов в учебные группы"""
    products = Product.objects.select_related('author').all()
    students = Student.objects.all()
    add_student_url = reverse('add_student')
    get_products_json = reverse('all_products')
    get_student_lessons_json = reverse('lessons')
    context = {'products': products,
               'students': students,
               'add_student_url': add_student_url,
               'all_products_json': get_products_json,
               'get_user_lessons_json': get_student_lessons_json}
    return render(request, 'products/index.html', context)
