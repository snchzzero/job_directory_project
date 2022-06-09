from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('currentemployees/', views.currentemployees, name='current_employees'),  # отображение всех созданых сотрудников
    path('createemployees/', views.createemployees, name='create_employees'),  # добавить сотрудника
    path('viewemployees/<int:employees_pk>', views.viewemployees, name='view_employees'),  # <int:employees_pk>/ - в адрес автомат-ки подставляет значение
    path('deleteemployee/<int:employee_pk>', views.deleteemployee, name='delete_employee'),
]



