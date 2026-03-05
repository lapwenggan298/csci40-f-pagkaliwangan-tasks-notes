from django import forms
from .models import TaskGroup

class TaskForm(forms.Form):
    name = forms.CharField(label = "Task Name",max_length=100)
    due_date = forms.DateTimeField(label = "Due Date")
    taskgroup = forms.ModelChoiceField(
        label="Task Group",
        queryset=TaskGroup.objects.all()
    )
