from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from config.forms import TagForm, TaskForm
from config.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "config/index.html"
    paginate_by = 5

    def get_queryset(self):
        return Task.objects.all().order_by("is_done", "-datetime")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("config:index")
    template_name = "config/task_form.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("config:index")
    template_name = "config/task_form.html"


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("config:index")


class TaskToggleStatusView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("config:index")


class TagListView(generic.ListView):
    model = Tag
    template_name = "config/tag_list.html"
    paginate_by = 5

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
