from django.db import models

from django.urls import reverse
# Create your models here.
#This is a relational database, so the databases have a relationship.

class TaskGroup(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=100) #max
    due_date =  models.DateTimeField(null=False) #Due Date will always appear
    #Foreign Key should be here, because we only want to have one instance of a group. One instance of a category of tasks.
    taskgroup = models.ForeignKey(
        TaskGroup,
        on_delete=models.CASCADE, #when the group is removed, the task models inside it are also removed, if on_delete=models.NULL, only the task group is removed.
        related_name='tasks', #will be used when you want to get it/obtain from a TaskGroup.
        )
    #March 9, 2026
    task_image = models.ImageField(
	upload_to='images/',
	null = True,
    )
    #per-instance level methods if they are in classes
    def __str__(self): #dunder = double underscore, if you print out the thing as is, it will return its string value (?).
        return f"{self.name} due on {self.due_date}"
        #return "{} due on {}".format(self.name, self.due_date)

    def get_absolute_url(self): #gets the absolute url, if there is an active instance, it will return the absolute url.
        return reverse('tasks:task_detail', args=[str(self.id)]) #app:--_detail', return the reverse/url of the --_-- in the app urls.py.
    
    class Meta: #metadata about the class on how it should behave, you can alsoo add attributes.
        verbose_name = "task"
        verbose_name_plural = "tasks"
        #unique_together = ['due_date', 'name'] there must only be one unique/do not create a duplicate task.




