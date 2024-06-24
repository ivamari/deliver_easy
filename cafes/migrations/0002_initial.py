# Generated by Django 4.2.13 on 2024-06-23 20:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cafes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders_user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='employee',
            name='cafe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees_info', to='cafes.cafe'),
        ),
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employees_info', to='cafes.cafedepartment'),
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='position_employees', to='cafes.position', verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cafes_info', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cartproduct',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_products', to='cafes.cart', verbose_name='Корзина пользователя'),
        ),
        migrations.AddField(
            model_name='cartproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_carts', to='cafes.product', verbose_name='Продукт'),
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(through='cafes.CartProduct', to='cafes.product', verbose_name='Продукты'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_cart', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cafeproduct',
            name='cafe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_cafe', to='cafes.cafe', verbose_name='Кафе'),
        ),
        migrations.AddField(
            model_name='cafeproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cafe_products', to='cafes.product', verbose_name='Продукты'),
        ),
        migrations.AddField(
            model_name='cafedepartment',
            name='cafe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cafe_departments', to='cafes.cafe'),
        ),
        migrations.AddField(
            model_name='cafedepartment',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cafe_departments', to='cafes.department', verbose_name='Название отдела'),
        ),
        migrations.AddField(
            model_name='cafedepartment',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='departments_manager', to=settings.AUTH_USER_MODEL, verbose_name='Менеджер'),
        ),
        migrations.AddField(
            model_name='cafedepartment',
            name='members',
            field=models.ManyToManyField(related_name='departments_members', to=settings.AUTH_USER_MODEL, verbose_name='Сотрудники отдела'),
        ),
        migrations.AddField(
            model_name='cafe',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='CREATED_%(app_label)s_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='cafe',
            name='departments',
            field=models.ManyToManyField(blank=True, through='cafes.CafeDepartment', to='cafes.department', verbose_name='Отделы'),
        ),
        migrations.AddField(
            model_name='cafe',
            name='employees',
            field=models.ManyToManyField(blank=True, related_name='cafes_employees', through='cafes.Employee', to=settings.AUTH_USER_MODEL, verbose_name='Сотрудники'),
        ),
        migrations.AddField(
            model_name='cafe',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='cafes_owners', to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
        migrations.AddField(
            model_name='cafe',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(app_label)s_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Updated by'),
        ),
        migrations.AddConstraint(
            model_name='cafedepartment',
            constraint=models.UniqueConstraint(fields=('department', 'manager'), name='unique_department_manager'),
        ),
        migrations.AlterUniqueTogether(
            name='cafe',
            unique_together={('name', 'location')},
        ),
    ]
