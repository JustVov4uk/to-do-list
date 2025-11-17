from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from config.forms import TagForm
from config.models import Task, Tag


def index(request: HttpRequest) -> HttpResponse:
    num_tasks = Task.objects.count()

    context = {"num_tasks": num_tasks}
    return render(request, "config/index.html", context=context)


class TaskListView(generic.ListView):
    model = Task


class TagListView(generic.ListView):
    model = Tag
    template_name = "config/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("config:tag-list")
    template_name = "config/tag_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("config:tag-list")
    template_name = "config/tag_form.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("config:tag-list")
    template_name = "config/tag_confirm_delete.html"
