from django.contrib import admin

from .models import Task, TaskGroup

# Register your models here. Uses Models
class TaskInLine(admin.TabularInline): #adds the ability to add tasks in the task group via admin?
    model = Task

class TaskGroupAdmin(admin.ModelAdmin): #The TaskGroup "Tab"
    model = TaskGroup
    inlines = [TaskInLine]

class TaskAdmin(admin.ModelAdmin):
    model = Task
    search_fields = ['name',] #adds a search field in task admin in tuples
    list_display = ['name', 'due_date',] #displays the name and due date instead of the default name date
    list_filter = ['due_date',] #adds a filter by due date

    fieldsets = [
        ('Details', {
            'fields': [
                ('name', 'taskgroup'), 'due_date', #if two things are inside, that means they will be in the same line, the separated ones will be on a new line
            ]
        })
    ]

admin.site.register(TaskGroup, TaskGroupAdmin)
admin.site.register(Task, TaskAdmin)