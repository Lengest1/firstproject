from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def index(request):
    return HttpResponse('<b>Главная страница</b>')

def posts_list(request):
    return HttpResponse('Список постов')

def posts_details(request,index):
    return HttpResponse(f'Подробная информация {index}')

def groups_list(request):
    return HttpResponse('Список групп')

def group_info(request,any):
    return HttpResponse(f'Информация о группе {any}')
