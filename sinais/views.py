from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa

def home(request):
    x = Pessoa(nome='Pedro', email='pedro@gmail.com', telefone='32522353')
    x.save()
    return HttpResponse('Home')