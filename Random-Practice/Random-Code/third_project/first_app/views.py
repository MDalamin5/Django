from django.shortcuts import render

# Create your views here.

def contact(request):
    return render(request, './first_app/index.html' , {"name" : "Md Al Amin", "marks" : 86, "lst" : [24,3, 10, 5], "blog" : "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.", "courses" : [
        {
            'id' : 1,
        'course' : 'C',
        'teacher' : 'Al Amin'
        },
        {
            
            'id' : 2,
        'course' : 'Cpp',
        'teacher' : 'Kaysar'
        },
        {
            
            'id' : 3,
        'course' : 'Django',
        'teacher' : 'Phitron'
        },
    ]} )


