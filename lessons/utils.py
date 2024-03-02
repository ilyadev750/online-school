from .models import Group
import random


def get_the_group(product_obj, student_obj):
    """Получить группу, в которую распределить студента.
    Если групп нет или они заполнены, создать новые три
    """
    groups = (Group.objects.select_related('product_id')
              .select_related('lector_id')
              .prefetch_related('student')
              .filter(product_id=product_obj, quantity__lt=2)
              .order_by('-quantity'))
    if not groups:
        for _ in range(3):
            new_group = create_new_group(product_obj=product_obj)
            new_group.save()
        new_group = add_student_in_group(group=new_group,
                                         student_obj=student_obj)
        return new_group
    group = groups[0]
    group = add_student_in_group(group=group, student_obj=student_obj)
    return group


def add_student_in_group(group, student_obj):
    """Добавить студента в группу"""
    group.student.add(student_obj)
    group.quantity += 1
    return group


def create_new_group(product_obj):
    """Создать новую группу"""
    new_group = Group()
    new_group.group_name = (f'{product_obj.product_name} '
                            f'- группа № {random.randint(1, 10000)}')
    new_group.product_id = product_obj
    new_group.lector_id = product_obj.author
    new_group.quantity = 0
    return new_group
