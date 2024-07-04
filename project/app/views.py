from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse, FileResponse
from .serializers import Taskserializer, Userserializer
import pandas as pd
from io import BytesIO

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'user.html', {'form': form})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task.html', {'form': form})

def user_list(request):
    users = User.objects.all()

    paginator = Paginator(users, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    Context={
        'page_obj': page_obj,
        'data':users
    }
    return render(request, 'user_list.html', Context)

def task_list(request):
    tasks = Task.objects.all()
    paginator = Paginator(tasks, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    Context={
        'page_obj': page_obj,
        'taskdata':tasks
    }
    return render(request, 'task_list.html',Context )

def export_to_excel(request):
    tasks = Task.objects.all()
    serializer = Taskserializer(tasks, many=True) 
    df = pd.DataFrame(serializer.data)  
    excel_file = BytesIO()  
    df.to_excel(excel_file, index=False, engine='openpyxl')  
    excel_file.seek(0) 
    response = HttpResponse(excel_file, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=tasks.xlsx'
    return response


def user_to_excel(request):
    user = User.objects.all()
    serializer = Userserializer(user, many=True)
    print(serializer) 
    df = pd.DataFrame(serializer.data)  
    user_excel = BytesIO()  
    df.to_excel(user_excel, index=False, engine='openpyxl')  
    user_excel.seek(0) 
    response = HttpResponse(user_excel, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=tasks.xlsx'
    return response

