# Generated by Django 4.2.13 on 2024-06-07 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafes', '0002_cart_category_department_employee_order_orderstatus_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cooking_time',
            field=models.IntegerField(default=1, verbose_name='Время приготовления'),
            preserve_default=False,
        ),
    ]