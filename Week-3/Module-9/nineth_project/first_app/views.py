from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse

# Create your views here.

def home(request):
    response = render(request, 'home.html')
    response.set_cookie('name', 'Md Al Amin', expires=datetime.utcnow()+timedelta(days=7))
    return response

def get_cooki(request):
    name = request.COOKIES.get('name')
    return render(request, 'get.html', {'name' : name})



def del_cooki(request):
    resposne = render(request, 'del.html')
    resposne.delete_cookie('name')
    return resposne

# session vs cooki
# cooki one kind of clint database or user or visitor data base his browser
# session is the website data base where user importent data save in web-site main database
# session for authentication
# cooki: in our website what you want to see in our website, remmber me ai doranr jonno


def set_session(request):
    # data = {
    #     'name' : 'Md Al Amin', 
    #     'age' : 23,
    #     'language' : 'Bangggggla'
    # }
    # print(request.session.get_session_cookie_age())
    # print(request.session.get_expiry_date())

    # request.session.update(data)
    request.session['name'] = 'Al Amin'
    return render(request, 'home.html')


# this function is no same as the course instructior
def get_session(request):
    if 'name' in request.session:
        data = request.session
        request.session.modified = True
        return render(request, 'get.html', {'data' : data})
    else:
        return HttpResponse("Your session is expired. Login againg")


# instructor function

# def get_seesion(request):
#     name = request.session.get('name')
#     age = request.session.get('age')
#     language = request.session.get('language')
#     return render(request, 'get.html', {'name': name, 'age' : age})


def delete_Session(request):
    request.session.flush()
    return render(request, 'del.html')

