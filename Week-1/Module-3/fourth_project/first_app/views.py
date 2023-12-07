from django.shortcuts import render

# Create your views here.

def contact(request):
    return render(request, 'f_app/home.html', {'name' : 'I am Rahim', 'marks' : 86,
                                                'courses' : [
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
    ]})

def about(request):
    return render(request, 'f_app/about.html')
