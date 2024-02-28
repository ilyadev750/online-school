from django.db import models
from datetime import datetime
from users.models import Author, Username


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Название продукта')
    start_date = models.DateTimeField(default=datetime.now(), verbose_name='Начало')
    price = models.IntegerField(verbose_name='Цена')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор курса')
    
    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукт'

    def __str__(self):
        return f'{self.product_name}'


class Purchase(models.Model):
    username = models.ForeignKey(Username, on_delete=models.CASCADE, verbose_name='Пользователь')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    status = models.BooleanField(verbose_name='Статус оплаты')

    class Meta:
        verbose_name = 'Статус оплаты'
        verbose_name_plural = 'Статусы оплаты'
        unique_together = ('username', 'product_id',)