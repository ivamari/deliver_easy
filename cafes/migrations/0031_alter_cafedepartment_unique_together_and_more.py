# Generated by Django 4.2.13 on 2024-06-21 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafes', '0030_alter_cafedepartment_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cafedepartment',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='cafedepartment',
            constraint=models.UniqueConstraint(fields=('department', 'manager'), name='unique_department_manager'),
        ),
    ]