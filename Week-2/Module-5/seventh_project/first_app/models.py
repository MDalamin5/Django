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
        ordering = ['id']


# One to One Relationship BuildUp
class Person(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"


class Passport(models.Model):
    user = models.OneToOneField(to=Person, on_delete= models.CASCADE)
    pass_number = models.IntegerField()
    page = models.IntegerField()
    validity = models.IntegerField()
    class Meta:
        ordering = ['id']


# One to many Relationship  1----->m : Person-------Post
class Post(models.Model):
    user = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, related_name='posts')
    post_cap = models.CharField(max_length=100)
    post_details = models.CharField(max_length=500)


# many to many Relationship

class Student(models.Model):
    name = models.CharField(max_length=40)
    roll = models.IntegerField()
    class_name = models.CharField(max_length=10)
    
    class Meta:
        ordering = ['id']

    def __str__(self) -> str:
        return self.name

class Teacher(models.Model):
    student = models.ManyToManyField(Student, related_name='teachers')
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=30)
    mobile = models.CharField(max_length=11)

    def student_list(self):
        return ",".join([str(i) for i in self.student.all()])



