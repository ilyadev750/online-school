# Generated by Django 4.2.7 on 2024-02-28 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='username',
            options={'verbose_name': 'Студент', 'verbose_name_plural': 'Студенты'},
        ),
        migrations.AlterModelTable(
            name='author',
            table='Авторы',
        ),
        migrations.AlterModelTable(
            name='username',
            table='Студенты',
        ),
    ]
