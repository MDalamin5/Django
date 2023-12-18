from django.shortcuts import render

# Create your views here.

def feedback(request):
    return render(request, './first_app/index.html', {'courses' : [
        {
            'id' : 1,
            'course' : 'C',
            'teacher' : 'Rahim'
        },
        {
            'id' : 2,
            'course' : 'C++',
            'teacher' : 'KhaRahim'
        },
        {
            'id' : 3,
            'course' : 'Python',
            'teacher' : 'Fahim'
        }
    ],
        'marks' : 86,
        'list' : [24, 3, 10, 5],
        'blog' : "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
        'name' : 'Md Al Amin',
        'age' : 23
    })
