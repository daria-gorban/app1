from turtle import title
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {"title": "Главная", "dev_guys": ["Петя", "Вася"]}
    return render(request, "main/index.html", context)


def about(request):
    return HttpResponse("About page")
