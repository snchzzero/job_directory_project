# Generated by Django 4.0.5 on 2022-06-10 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_employees_models_employees_models_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees_models',
            name='employees_Models_age',
            field=models.PositiveSmallIntegerField(blank=True, max_length=50),
        ),
    ]