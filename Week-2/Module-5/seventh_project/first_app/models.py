from django.db import models

# Create your models here.

class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30)
    address = models.TextField()

    def __str__(self) -> str:
        return f"Roll: {self.roll}  Name: {self.name}"


"""
        1. Model Inharetance
        2. Multitable Inharitance
        3. proxy Model

        1. abstract base class
"""
 # abstract Base Class
class CommonInfoClass(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=40)
    class Meta:
        abstract = True

class StudentInfoModel(CommonInfoClass):
    roll = models.IntegerField(null=True)
    payment = models.IntegerField()
    section = models.CharField(max_length=70)



class TeacherInfoModel(CommonInfoClass):
    salary = models.IntegerField()


# multitable Inharitance

class EmployeeModel(models.Model):
    name = models.CharField(max_length=70)
    city = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)

class ManagerModel(EmployeeModel):
    take_interview = models.BooleanField()
    hiring = models.BooleanField()


#3 Proxy Model

class FriendModel(models.Model):
    school = models.CharField(max_length=50)
    section = models.CharField(max_length=10)
    attendence = models.BooleanField()
    home_work = models.CharField(max_length=500)
    

class MeModel(FriendModel):
    class Meta:
        proxy = True

        