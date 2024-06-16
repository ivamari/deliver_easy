# Generated by Django 4.2.13 on 2024-06-16 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cafes', '0025_category_cooking_time_delete_categorycookingtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions_department', to='cafes.department', verbose_name='Отдел'),
        ),
    ]
