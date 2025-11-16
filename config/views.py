from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from config.models import Task


def index(request: HttpRequest) -> HttpResponse:
    num_tasks = Task.objects.count()

    context = {"num_tasks": num_tasks}

    return render(request, "config/index.html")

