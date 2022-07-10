from django.http import HttpResponse
from django.shortcuts import render
from numpy import character
import random

# Create your views here.


def index(request):

    return render(request, './index.html')


def password(request):

    # 英文字母小寫
    characters = [chr(i) for i in range(97, 123)]

    if request.POST.get('uppercase'):
        characters += [chr(i) for i in range(65, 91)]

    if request.POST.get('numbers'):
        characters += list('0123456789')

    if request.POST.get('special'):
        characters += list('@#$%^&*')

    length = eval(request.POST.get('input-length')) \
        if request.POST.get('input-length') else eval(request.POST.get('length'))

    password = ''.join([random.choice(characters) for i in range(length)])

    return render(request, './password.html', {'password': password})
