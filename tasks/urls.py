from django.urls import path

from .views import index, task_list, TaskListView, task_detail, TaskDetailView

urlpatterns = [
	path('', index, name = "index"),
    path('list', TaskListView.as_view(), name = "task-list"), #TaskListView.as_view(), task_list
    path('<int:pk>', TaskDetailView.as_view(), name = "task_detail"), #task_detail
]

#This might be needed, depending on your Django version
app_name = "tasks"
