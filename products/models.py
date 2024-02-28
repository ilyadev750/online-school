from django.db import models
from datetime import datetime
from users.models import Author, Student


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Название продукта')
    start_date = models.DateTimeField(default=None, verbose_name='Начало')
    price = models.IntegerField(verbose_name='Цена')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор курса')

    
    class Meta:
        db_table = 'product'
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукт'

    def __str__(self):
        return f'{self.product_name}'


class Purchase(models.Model):
    username = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Пользователь')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    status = models.BooleanField(verbose_name='Статус оплаты')

    class Meta:
        db_table = 'purchase'
        verbose_name = 'Статус оплаты'
        verbose_name_plural = 'Статусы оплаты'
        unique_together = ('username', 'product_id',)