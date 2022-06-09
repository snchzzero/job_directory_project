from django.db import models

class employees(models.Model):
    employees_FIO = models.CharField(max_length=100)
    employees_age = models.CharField(max_length=100)

    def __str__(self):  # функция в отображении панели админа возращает не номера проектов, а заголовок проекта
        return self.job_title