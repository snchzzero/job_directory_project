from django.db import models

class Job(models.Model):
    job_title = models.CharField(max_length=100)  # в заголовках небольше 100символов
    job_category = models.CharField(max_length=100)

    emplayees_FIO = models.CharField(max_length=100)
    emplayees_age = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now=True)  # отображается не только дата, но и время
    # auto_now=True - атрибут присваивается автоматически

    def __str__(self):  # функция в отображении панели админа возращает не номера проектов, а заголовок проекта
        return self.job_title