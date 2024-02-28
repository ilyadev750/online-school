from django.db import models


class Username(models.Model):
    username = models.CharField(max_length=100, verbose_name='Никнейм', unique=True)
    name = models.CharField(max_length=100, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.username}'

    
class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя автора')
    surname = models.CharField(max_length=100, verbose_name='Фамилия автора')
    patronymic = models.CharField(max_length=100, verbose_name='Отчество автора')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        unique_together = ('name', 'surname', 'patronymic')

    def __str__(self):
        return f'{self.surname} {self.name[0]}.{self.patronymic[0]}.'