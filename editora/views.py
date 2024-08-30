from django.shortcuts import render, redirect, get_object_or_404
from . import models
from ninja import Router

api = Router()

def home(request):
    editoras = models.Editora.objects.all()
    return render(request, 'home.html', {'editoras': editoras})