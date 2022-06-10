from django.shortcuts import render, redirect, get_object_or_404
from .models import employees_Models
from .forms import employeesForm
from job.models import Job

def createemployees(request):
    currentjobs = Job.objects.all()
    if request.method == 'GET':
        return render(request, 'employees/create_employees.html', {'form':employeesForm(), 'currentjobs':currentjobs})
    else:
        try:
            # выполняется если пользователь внес какую-то информацию в окно и нажал кнопку Create (Создать)
            form =employeesForm(request.POST)  # соединить внесенную информацию с нашей формой
            newemployees = form.save(commit=False)  # даная форму сохраняет информацию в базу данных
            # делаем привязку созданной записи к конкрутному пользователю
            newemployees.user = request.user
            newemployees.save()  # сохранит привязку в БД
            return redirect('employees:current_employees')  # перенаправить пользователя на список доступных сотрудников
        except ValueError:
            # если вводимое название задачи "title" больше 100 символов, то возникает ошибка и мы ее обрабатываем
            return render(request, 'employees/create_employees.html',
                          {'form': employeesForm(), 'currentjobs':currentjobs, 'error': 'Bad data passed in. Try again'})
            # переданы неверные данные. попробуйте еще раз


def currentemployees(request):
    # пользователь видит все записи созданные всеми пользователями
    currentemployees = employees_Models.objects.all().order_by('employees_Models_LastName')
    return render(request, 'employees/current_employees.html', {'currentemployees':currentemployees})

def viewemployees(request, employees_pk):
    # pk-первичный ключ (поиск объекта из базы по номеру ключа)
    employees = get_object_or_404(employees_Models, pk=employees_pk)
    currentjobs = Job.objects.all()
    if request.method == 'GET':
        #для редактирования уже имеющийся заметки, записи
        form = employeesForm(instance=employees)  # instance=1todo - уточняем, что изменяем уже существующий объект
        return render(request, 'employees/view_employees.html',
                      {'employees': employees, 'form': form, 'currentjobs':currentjobs})
    else: # для сохранения отредактированой записи (заметки)
        try:
            form = employeesForm(request.POST, instance=employees)
            # соединить внесенную информацию с нашей формой, instance=1todo - уточняем, что изменяем уже существующий объект
            form.save()
            return redirect('employees:current_employees')  # перенаправить пользователя на список сотрудников
        except ValueError:
            return render(request, 'employees/view_employees.html', {'employees': employees, 'form': form, 'error': 'Bad info'})


def deleteemployee(request, employee_pk):  # удалить задачу может только тот пользователь, к-ый создавал ее
    employees = get_object_or_404(employees_Models, pk=employee_pk)
    if request.method == 'POST':
        employees.delete()
        return redirect('employees:current_employees')  # перенаправить пользователя на список должностей