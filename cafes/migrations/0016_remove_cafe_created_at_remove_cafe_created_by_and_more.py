# Generated by Django 4.2.13 on 2024-06-12 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cafes', '0015_remove_department_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cafe',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='cafe',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='cafe',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='cafe',
            name='updated_by',
        ),
    ]