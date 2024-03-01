from django.shortcuts import render, redirect
from .models import Student
from .utils import get_student, get_product, get_purchase_status, create_purchase_status_obj
from lessons.utils import get_the_group
from .forms import AddStudentForm


def add_student_to_product(request):
    product_name = request.GET.get('product_name')
    if request.method == 'POST':
        student_form = AddStudentForm(request.POST)
        if student_form.is_valid():
            product_obj = get_product(product_name=product_name)
            student_obj = get_student(form=student_form)
            if not product_obj or not student_obj:
                context = {'error': 'Студента или продукта с данным именем не существует!',
                           'form': AddStudentForm()}
                return render(request, 'users/add_student.html', context)
            purchased_status_obj = get_purchase_status(product_obj=product_obj,
                                                       student_obj=student_obj)
            if purchased_status_obj:
                context = {'error': 'Пользователь по данному курсу уже состоит в группе!',
                           'form': AddStudentForm()}
                return render(request, 'users/add_student.html', context)
            purchased_status_obj = create_purchase_status_obj(student_obj=student_obj, product_obj=product_obj)
            purchased_status_obj.save()
            group = get_the_group(product_obj=product_obj, student_obj=student_obj)
            group.save()
            return redirect('home')
    else:
        student_form = AddStudentForm()
        context = {'form': student_form}
        return render(request, 'users/add_student.html', context)
        
# проверить продукт на наличие в базе, взять студента из базы,
# проверить, что студент введен корректно, проверить статус оплаты или создать новый. После чего начать реализовывать
# распределение в группу в зависимости от даты курса, проверить все линтером
