from .models import Student
from products.models import Product, Purchase
from django.core.exceptions import ObjectDoesNotExist


def get_student_or_create_new(form):
    try:
        username = form.cleaned_data['username']
        student_obj = Student.objects.get(username=username)
        # if student_obj.
    except ObjectDoesNotExist:
        student_obj = Student()
        student_obj.username = form.cleaned_data['username']
        student_obj.surname = form.cleaned_data['surname']
        student_obj.name = form.cleaned_data['name']
    return student_obj


def get_purchase_status(form, product_obj):
    try:
        username = form.cleaned_data['username']
        purchased_status_obj = (Purchase.objects.select_related('username')
                                .select_related('product_id')
                                .get(product_id=product_obj, username=username))
    except ObjectDoesNotExist:
        purchased_status_obj = None
    return purchased_status_obj    


def get_product(form):
    try:
        product_name = form.cleaned_data['product_name']
        product_obj = (Product.objects.select_related('author')
                       .get(product_name=product_name))
    except ObjectDoesNotExist:
        product_obj = None
    return product_obj                  

    
