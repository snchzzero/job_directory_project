from django.db import models

class employees_Models(models.Model):
    employees_Models_LastName = models.CharField(max_length=100, blank=True)
    employees_Models_MidleName = models.CharField(max_length=100, blank=True)
    employees_Models_FirstName = models.CharField(max_length=100, blank=True)
    employees_Models_age = models.PositiveSmallIntegerField(blank=True)
    employees_Models_job = models.CharField(max_length=100, blank=True)

    def __str__(self):  # функция в отображении панели админа возращает не номера проектов, а заголовок проекта
        return self.employees_Models_FIO