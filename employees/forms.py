from django.forms import ModelForm
from .models import employees_Models  # модель для объектов

class employeesForm(ModelForm):
    class Meta:
        model = employees_Models
        fields = ['employees_Models_LastName', 'employees_Models_MidleName',
                  'employees_Models_FirstName', 'employees_Models_age']  # что будем отображать - список