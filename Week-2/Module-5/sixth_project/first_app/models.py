from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length= 40)
    roll = models.IntegerField(primary_key= True)
    addrss = models.TextField()
    father_name = models.TextField(default='No Name')

    def __str__(self) -> str:
        return f"Roll: {self.roll} Name: {self.name}"