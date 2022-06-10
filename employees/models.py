from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

class employees_Models(models.Model):
    # RegexValidator - регулярное выражение на проверку имени
    employees_Models_LastName = models.CharField(max_length=30, blank=True,
                                                 validators=[RegexValidator(r'^[a-zA-Zа-яА-Я]')])
    employees_Models_MidleName = models.CharField(max_length=30, blank=True,
                                                  validators=[RegexValidator(r'^[a-zA-Zа-яА-Я]')])
    employees_Models_FirstName = models.CharField(max_length=30, blank=True,
                                                  validators=[RegexValidator(r'^[a-zA-Zа-яА-Я]')])
    employees_Models_gender = models.CharField(max_length=10, blank=True)

    # проверка возраста от 14 до 99 лет
    employees_Models_age = models.IntegerField(blank=True, validators=[MinValueValidator(14), MaxValueValidator(99)])
    employees_Models_job = models.CharField(max_length=70, blank=True)

    def __str__(self):  # функция в отображении панели админа возращает не номера проектов, а заголовок проекта
        return self.employees_Models_FIO