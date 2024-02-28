from django.shortcuts import render
from .models import Student
from .utils import get_student_or_create_new, get_product, get_purchase_status
from products.models import Purchase, Product
from .forms import AddStudentForm
from django.core.exceptions import ObjectDoesNotExist


def add_student_to_product(request):
    if request.method == 'POST':
        student_form = AddStudentForm(request.POST)
        product_obj = get_product(form=student_form)
        if not product_obj:
            context = {'error': 'Продукта с данным именем не существует!'}
            return render(request, 'users/add_student.html', context)
        
        student_obj = get_student_or_create_new(form=student_form)

        purchased_status_obj = get_purchase_status(form=student_form, product_obj=product_obj)
        if purchased_status_obj:
            context = {'error': 'Пользователь по данному курсу уже состоит в группе!'}
            return render(request, 'users/add_student.html', context)
        
# реализовать форму по добавлению студента в базу, проверить продукт на наличие в базе, взять студента из базы,
# проверить, что студент введен корректно, проверить статус оплаты или создать новый. После чего начать реализовывать
# распределение в группу в зависимости от даты курса, проверить все линтером



        # try:
        #     username = student_form.cleaned_data['username']
        #     purchased_status_obj = (Purchase.objects.select_related('username')
        #                             .select_related('product_id')
        #                             .get(product_id=product_obj, username=username))
        #     context = {'error': 'Пользователь по данному курсу уже состоит в группе!'}
        #     return render(request, 'users/add_student.html', context)
        # except ObjectDoesNotExist:
            


        # try:
        #     purchased_status_obj = (Purchase.objects.select_related('username')
        #                         .select_related('product_id')
        #                         .get(product_id__product_name=product_name))
        # product_name = student_form.cleaned_data['product']
        #     try:
        #         username = student_form.cleaned_data['username']
        #         student_obj = Student.objects.get(username=username)
        #     except ObjectDoesNotExist:
        #         student_obj = create_new_student(form=student_form)
        #         student_obj.save()
        #     try:
        #         purchased_status_obj = (Purchase.objects.select_related('username')
        #                             .select_related('product_id')
        #                             .get(product_id__product_name=product_name))
        #     except ObjectDoesNotExist:
        #         purchased_status_obj = Purchase()
        #         purchased_status_obj.username = student_obj
        #         purchased_status_obj.product_id = Product.objects.get(username=username)