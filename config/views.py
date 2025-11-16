from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from config.models import Task, Tag


def index(request: HttpRequest) -> HttpResponse:
    num_tasks = Task.objects.count()

    context = {"num_tasks": num_tasks}
    return render(request, "config/index.html", context=context)


class TaskListView(generic.ListView):
    model = Task


class TagListView(generic.ListView):
    model = Tag
