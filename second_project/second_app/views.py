from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def courses(request):
    return HttpResponse( '''
                        <h1>Wellcome to Courses Page</h1>
                        <a href = '/second_app/fidback/' > Fidback </a>
                        <a href = '/first_app/about/' > About </a>
                        <a href = '/first_app/contact/' > Contact </a>
                        ''')

def fidback(request):
    return HttpResponse(
                        '''
                        <h1>Wellcome to Fidback Page</h1>
                        <a href = '/second_app/courses/' > Courses </a>
                        <a href = '/first_app/about/' > About </a>
                        <a href = '/first_app/contact/' > Contact </a>
                        '''
                        )
