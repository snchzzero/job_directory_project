# Generated by Django 4.0.5 on 2022-06-10 08:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_alter_employees_models_employees_models_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees_models',
            name='employees_Models_FirstName',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='employees_models',
            name='employees_Models_LastName',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='employees_models',
            name='employees_Models_MidleName',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='employees_models',
            name='employees_Models_age',
            field=models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(14), django.core.validators.MaxValueValidator(99)]),
        ),
    ]
