
from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    
    pages = {
        'Главная страница': reverse('home-view'),
        'Показать текущее время': reverse('time-view'),
        'Показать содержимое рабочей директории': reverse('workdir-view')
    }
    
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):

    current_date_time = datetime.now()
    current_time = str(current_date_time.time())
    msg = f'Текущее время: {current_time[:8]}'
    return HttpResponse(msg)


def workdir_view(request):

    text = ', '.join(os.listdir())
    print(text)
    return HttpResponse(text)
