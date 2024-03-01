from django.db import models
from products.models import Product
from users.models import Student, Author
from django.core.validators import MinValueValidator, MaxValueValidator


class Lesson(models.Model):
    lesson_name = models.CharField(max_length=100, verbose_name='Название урока')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    video_link = models.CharField(max_length=200, verbose_name='Ссылка на урок')

    class Meta:
        db_table = 'lesson'
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        unique_together = ('lesson_name', 'product_id',)

    def __str__(self):
        return f'{self.lesson_name}'
    

class Group(models.Model):
    group_name = models.CharField(max_length=100, verbose_name='Название группы')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    lector_id = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Лектор')
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(3)])
    student = models.ManyToManyField(Student)

    def __str__(self):
        return f'{self.group_name}'
    
    class Meta:
        db_table = 'group'
        verbose_name = 'Учебная группа'
        verbose_name_plural = 'Учебные группы'
        unique_together = ('group_name', 'product_id',)

