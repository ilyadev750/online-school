# Generated by Django 4.2.7 on 2024-02-28 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_table_alter_purchase_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='product',
            table='product',
        ),
        migrations.AlterModelTable(
            name='purchase',
            table='purchase',
        ),
    ]
