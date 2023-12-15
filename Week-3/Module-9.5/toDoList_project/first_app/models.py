from django.db import models

# Create your models here.
class TaskMode(models.Model):
    taskTitle = models.CharField(max_length=50)
    taskDescription = models.CharField(max_length=300)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.taskTitle