# Generated by Django 4.0.5 on 2022-06-10 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0010_alter_employees_models_employees_models_firstname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees_models',
            name='employees_Models_gender',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
