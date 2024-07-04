from django.urls import path
from .views import *

urlpatterns = [
    path('add_user/', add_user, name='add_user'),
    path('add_task/', add_task, name='add_task'),
    path('user_list/', user_list, name='user_list'),
    path('task_list/', task_list, name='task_list'),
    path('export_to_excel/', export_to_excel, name='export_to_excel'),
    path('user_to_excel/', user_to_excel, name='user_to_excel'),
]

