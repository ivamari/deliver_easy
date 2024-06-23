# Generated by Django 4.2.13 on 2024-06-22 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cafes', '0031_alter_cafedepartment_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employees_info', to='cafes.cafedepartment'),
        ),
    ]
