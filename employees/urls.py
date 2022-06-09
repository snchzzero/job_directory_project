from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('currentemployees/', views.currentemployees, name='current_employees'),  # отображение всех созданых сотрудников
    path('createemployees/', views.createemployees, name='create_employees')  # добавить сотрудника
]



