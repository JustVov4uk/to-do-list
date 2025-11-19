from django.urls import path
from config.views import (TaskListView,
                          TagListView, TagCreateView,
                          TagUpdateView, TagDeleteView,
                          TaskCreateView,
                          TaskUpdateView, TaskDeleteView,
                          TaskToggleStatusView)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/toggle/<int:pk>/", TaskToggleStatusView.as_view(), name="task-toggle"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/update/<int:pk>/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/delete/<int:pk>/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "config"
