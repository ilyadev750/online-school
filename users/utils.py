from .models import Student
from products.models import Product, Purchase
from django.core.exceptions import ObjectDoesNotExist


def get_student(form):
    """Проверка существования студента и получение
    его объекта"""
    try:
        username = form.cleaned_data['username']
        surname = form.cleaned_data['surname']
        name = form.cleaned_data['name']
        student_obj = Student.objects.get(username=username)
        if (student_obj.username == username
                and student_obj.surname == surname
                and student_obj.name == name):
            return student_obj
        else:
            student_obj = None
    except ObjectDoesNotExist:
        student_obj = None
    return student_obj


def get_purchase_status(product_obj, student_obj):
    """Получение статуса оплаты. Если объект существует,
    то студент уже распределен в группу."""
    try:
        purchased_status_obj = (Purchase.objects.select_related('username')
                                .select_related('product_id')
                                .get(product_id=product_obj,
                                     username=student_obj))
    except ObjectDoesNotExist:
        purchased_status_obj = None
    return purchased_status_obj


def get_product(product_name):
    """Получение продукта, если он оплачен"""
    try:
        product_obj = (Product.objects.select_related('author')
                       .get(product_name=product_name))
    except ObjectDoesNotExist:
        product_obj = None
    return product_obj


def create_purchase_status_obj(student_obj, product_obj):
    """Создание статуса оплачено True для студента
    для упрощения демонстрации работы программы. Далее
    идет распределение в группу"""
    purchased_status_obj = Purchase()
    purchased_status_obj.username = student_obj
    purchased_status_obj.product_id = product_obj
    purchased_status_obj.status = True
    return purchased_status_obj
