# Generated by Django 4.2.7 on 2024-02-28 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_username_options_alter_author_table_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='author',
            table='author',
        ),
        migrations.AlterModelTable(
            name='username',
            table='student',
        ),
    ]
