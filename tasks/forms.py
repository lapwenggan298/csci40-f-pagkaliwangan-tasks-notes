from django import forms
from .models import TaskGroup, Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
	#Model based form, the forms will be the one who will handle all fields, less work compared to below (commented out). 
	#Since fields = '__all__', it will show all required fields.
	#Fields can be specified/limited similar to lab#4
	#You can edit/add widgets so that some forms will take on a different form if I remember correctly from the discussion.
	#I just don't remember how to edit/do it.

#class TaskForm(forms.Form):
#    name = forms.CharField(label = "Task Name",max_length=100)
#    due_date = forms.DateTimeField(
#        label = "Due Date",
#        widget=forms.TextInput(
#            attrs = {'type', 'datetime-local'}
#        )
#    )
#    taskgroup = forms.ModelChoiceField(
#        label="Task Group",
#        queryset=TaskGroup.objects.all()
#    )
