from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.base import TemplateView

#16th of February
from .models import Task
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
# Create your views here.

#23rd of February
from django.contrib.auth.mixins import LoginRequiredMixin

#5th of March
from .models import TaskGroup
from .forms import TaskForm
from django.views.generic.edit import CreateView, UpdateView

#tasks = [ "Task 1", "Task 2", "Task 3", "Task 4"]

def index(request):
    return render(request, 'index.html', {'name': 'world'})

def task_list(request): #all the tasks/list of tasks
    tasks = Task.objects.all()
    taskgroups = TaskGroup.objects.all()
    ctx = {
        "task_list" : tasks,
        "taskgroups": taskgroups
           }

    if request.method == "POST":
        t = Task()
        t.name = request.POST.get('task_name')
        t.due_date = request.POST.get('due_date')
        t.taskgroup = t.TaskGroup.objects.get(
            pk=request.POST.get('taskgroup')
            )
        t.save()

    return render(request, 'task_list.html', ctx)

    #if request.method == 'POST':
    #    tasks.append(request.POST.get('task_name'))
    #ctx = {"tasks":tasks}
    #return render(request, 'task_list.html', ctx)

def task_detail(request, pk): #just the singular task
    task = Task.objects.get(pk=pk) #Why pk=pk instead of just pk? 
    # pk (left side): This is the field lookup name — Django treats "pk" as a shortcut for the model’s primary key field, whatever it’s called (id, uuid, slug, etc.). 
    # pk (right side): This is a Python variable holding the value you want to match.
    # means:
    # "Filter where the primary key field equals the value stored in the variable pk."
    # Why not just pk?
    # get() in Django works like Python’s function(arg=value) syntax — it expects named parameters for filtering.
    ctx = { "tasks" : task }
    return render(request, 'task_list.html', ctx)

class TaskListView(ListView): #The parameter inside the () is the class  or module it is inheriting from. #ListView does not/cannot handle POST requests.
    model = Task
    template_name = 'task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['taskgroups'] = TaskGroup.objects.all()
        context['form'] = TaskForm
        return context

    def post(self, request, *args, **kwargs): #this function will handle the POST
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            #t = Task()
            #t.name = request.POST.get('task_name')
            #t.due_date = request.POST.get('due_date')
            #t.taskgroup = TaskGroup.objects.get(
            #    pk=request.POST.get('taskgroup')
            #    )
            #t.save()

        return self.get(request, *args, **kwargs)


class TaskDetailView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "task_detail.html"
    form_class = TaskForm


class TaskCreateView(CreateView):
    model = Task
    template_name = "task_detail.html"
    form_class = TaskForm

# class TaskListView(TemplateView):
#     template_name = 'task_list.html'
    
#     kwargs is keyword arguments
#     def get_context_data(self, **kwargs):
#         return super().get_context_data(**kwargs)
#        context = super().get_context_data(**kwargs)

#        context['tasks'] = tasks
#        return context

#     def post(self, request, *args, **kwargs):
#        print(request.POST.get('task_name'))
#         ctx = self.get_context_data(**kwargs)
#         ctx['tasks'].append(request.POST.get('task_name'))
#         return render(request, self.template_name, ctx)
#        tasks.append(request.POST.get('task_name'))
#        return self.get(request, *args, **kwargs)
        
