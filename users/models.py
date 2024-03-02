from django.db import models


class Student(models.Model):
    """Модель студента"""
    username = models.CharField(max_length=100,
                                verbose_name='Никнейм',
                                unique=True)
    surname = models.CharField(max_length=100,
                               verbose_name='Фамилия')
    name = models.CharField(max_length=100,
                            verbose_name='Имя')

    class Meta:
        db_table = 'student'
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return f'{self.username}'


class Author(models.Model):
    """Модель автора/преподавателя продукта"""
    surname = models.CharField(max_length=100,
                               verbose_name='Фамилия автора')
    name = models.CharField(max_length=100,
                            verbose_name='Имя автора')
    patronymic = models.CharField(max_length=100,
                                  verbose_name='Отчество автора')

    class Meta:
        db_table = 'author'
        verbose_name = 'автор'
        verbose_name_plural = 'Авторы'
        unique_together = ('name', 'surname', 'patronymic')

    def __str__(self):
        return f'{self.surname} {self.name[0]}.{self.patronymic[0]}.'
