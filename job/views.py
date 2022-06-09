from django.shortcuts import render, redirect, get_object_or_404
from .forms import JobTitleForm  # импортируем нашу форму для страницы создания должностей пользователя createtodo
from .models import Job

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
            return redirect('current_job')  # перенаправить пользователя на список доступных должностей
        except ValueError:
            # если вводимое название задачи "title" больше 100 символов, то возникает ошибка и мы ее обрабатываем
            return render(request, 'job/create_job_title.html', {'form': JobTitleForm(), 'error': 'Bad data passed in. Try again'})
            # переданы неверные данные. попробуйте еще раз

def currentjob(request):
    # пользователь видит все записи созданные всеми пользователями
    currentjobs = Job.objects.all().order_by('job_title')
    return render(request, 'job/current_job.html', {'currentjobs': currentjobs})

def viewjob(request, job_pk):
    # pk-первичный ключ (поиск объекта из базы по номеру ключа)
    job = get_object_or_404(Job, pk=job_pk)

    if request.method == 'GET':
        #для редактирования уже имеющийся заметки, записи
        form = JobTitleForm(instance=job)  # instance=1todo - уточняем, что изменяем уже существующий объект
        return render(request, 'job/view_job.html', {'job': job, 'form': form})
    else: # для сохранения отредактированой записи (заметки)
        try:
            form = JobTitleForm(request.POST, instance=job)
            # соединить внесенную информацию с нашей формой, instance=1todo - уточняем, что изменяем уже существующий объект
            form.save()
            return redirect('current_job')  # перенаправить пользователя на список записей
        except ValueError:
            return render(request, 'job/view_job.html', {'job': job, 'form': form, 'error': 'Bad info'})

def deletejob(request, job_pk):  # удалить задачу может только тот пользователь, к-ый создавал ее
    job = get_object_or_404(Job, pk=job_pk)
    if request.method == 'POST':
        job.delete()
        return redirect('current_job')  # перенаправить пользователя на список должностей


