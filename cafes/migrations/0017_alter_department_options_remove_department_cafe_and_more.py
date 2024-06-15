# Generated by Django 4.2.13 on 2024-06-12 19:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cafes', '0016_remove_cafe_created_at_remove_cafe_created_by_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': 'Отдел', 'verbose_name_plural': 'Отделы'},
        ),
        migrations.RemoveField(
            model_name='department',
            name='cafe',
        ),
        migrations.RemoveField(
            model_name='department',
            name='manager',
        ),
        migrations.RemoveField(
            model_name='department',
            name='members',
        ),
        migrations.AddField(
            model_name='department',
            name='description',
            field=models.TextField(default=1, verbose_name='Описание отдела'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='CafeDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cafe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cafe_departments', to='cafes.cafe')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cafes', to='cafes.department', verbose_name='Название отдела')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='departments_manager', to=settings.AUTH_USER_MODEL, verbose_name='Менеджер')),
                ('members', models.ManyToManyField(blank=True, related_name='departments_members', to=settings.AUTH_USER_MODEL, verbose_name='Сотрудники отдела')),
            ],
            options={
                'verbose_name': 'Отдел',
                'verbose_name_plural': 'Отделы',
            },
        ),
        migrations.AddField(
            model_name='cafe',
            name='departments',
            field=models.ManyToManyField(blank=True, related_name='cafe_departments', through='cafes.CafeDepartment', to='cafes.department', verbose_name='Отделы'),
        ),
    ]
