from django.shortcuts import render
from first_app.forms import StudentForm
from . models import Teacher, Student, Person

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print(form.cleaned_data)
    else:
        form = StudentForm()
    return render(request, 'index.html', {'form' : form})


def show_data(request):
    # student list in one teacher
    # teacher = Teacher.objects.get(name = 'MUU')
    # students = teacher.student.all()
    # for stu in students:
    #     print(stu.name)

    """_summary_

    Descriptions:
        Teacher list in one student
        
    """
    # # process One
    # student = Student.objects.get(name = 'Al Amin')
    # teachers = student.teacher_set.all()
    # for tech in teachers:
    #     print(tech.name)

    # process Two
    student = Student.objects.get(name = 'Al Amin')
    teachers = student.teachers.all()
    print('Teacher Info')
    for tech in teachers:
        print(f"Teacher Name: {tech.name}, Subject: {tech.subject}, Mobile: {tech.mobile}")

    person = Person.objects.all()
    for per in person:
        print(per.name)

    # # this is practice function
    # poster_w = Person.objects.get(name = 'Md Al Amin')
    # post = poster_w.posts.all()
    # for pos in post:
    #     print(pos.post_cap)



    return render(request, 'show_data.html')
