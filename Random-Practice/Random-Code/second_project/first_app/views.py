from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def contact(request):
    return HttpResponse('''
                        <h1>Wellcome to Contact Page</h1>
                        <a href = '/first_app/about/' > About </a>
                        <a href = '/second_app/fidback/' > Fidback </a>
                        <a href = '/second_app/courses/' > Courses </a>
                        '''
                        )

def about(request):
    return HttpResponse(
                        '''
                        <h1>Wellcome to About Page</h1>
                        <a href = '/first_app/contact/' > Contact </a>
                        <a href = '/second_app/fidback/' > Fidback </a>
                        <a href = '/second_app/courses/' > Courses </a>
                        '''
                        )
