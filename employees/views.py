from django.shortcuts import render, redirect
from .models import employees_Models
from .forms import employeesForm

def createemployees(request):
    if request.method == 'GET':
        return render(request, 'employees/create_employees.html', {'form':employeesForm()})
    else:
        try:
            # выполняется если пользователь внес какую-то информацию в окно и нажал кнопку Create (Создать)
            form =employeesForm(request.POST)  # соединить внесенную информацию с нашей формой
            newemployees = form.save(commit=False)  # даная форму сохраняет информацию в базу данных
            # делаем привязку созданной записи к конкрутному пользователю
            newemployees.user = request.user
            newemployees.save()  # сохранит привязку в БД
            return redirect('current_employees')  # перенаправить пользователя на список доступных сотрудников
        except ValueError:
            # если вводимое название задачи "title" больше 100 символов, то возникает ошибка и мы ее обрабатываем
            return render(request, 'employees/create_employees.html', {'form': employeesForm(), 'error': 'Bad data passed in. Try again'})
            # переданы неверные данные. попробуйте еще раз





def currentemployees(request):
    return render(request, 'employees/current_employees.html')
