from django.contrib import admin
from .models import Job

class JobAdmin(admin.ModelAdmin):  # класс наследующий от модуля админ
    readonly_fields = ('created',)

admin.site.register(Job, JobAdmin)
# Register your models here.
