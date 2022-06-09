from django.forms import ModelForm
from .models import Job  # модель для объектов

class JobTitleForm(ModelForm):
    class Meta:
        model = Job
        fields = ['job_title', 'job_category']  # что будем отображать - список