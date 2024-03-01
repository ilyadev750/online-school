from django.shortcuts import render
from .models import Product
from django.urls import reverse


def index(request):
    products = Product.objects.select_related('author').all()
    add_student_url = reverse('add_student')
    context = {'products': products,
               'add_student_url': add_student_url}
    return render(request, 'products/index.html', context)
    
