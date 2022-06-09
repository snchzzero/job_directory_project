from django.shortcuts import render, redirect
from .forms import JobTitleForm  # импортируем нашу форму для страницы создания должностей пользователя createtodo

def home(request):
    return render(request, 'job/home.html')

def createjobtitle(request):
    if request.method == 'GET':
        return render(request, 'job/create_job_title.html', {'form': JobTitleForm()})
    else:
        try:
            # выполняется если пользователь внес какую-то информацию в окно и нажал кнопку Create (Создать)
            form =JobTitleForm(request.POST)  # соединить внесенную информацию с нашей формой
            newjobtitle = form.save(commit=False)  # даная форму сохраняет информацию в базу данных
            # делаем привязку созданной записи к конкрутному пользователю
            newjobtitle.user = request.user
            newjobtitle.save()  # сохранит привязку в БД
            return redirect('home')  # перенаправить пользователя на список записей
        except ValueError:
            # если вводимое название задачи "title" больше 100 символов, то возникает ошибка и мы ее обрабатываем
            return render(request, 'todo/createtodo.html', {'form': JobTitleForm(), 'error': 'Bad data passed in. Try again'})
            # переданы неверные данные. попробуйте еще раз


def createemplayees(request):
    return render(request, 'job/create_emplayees.html')
