from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def contact(request):
#     return HttpResponse('Hi! This is Contact page')

def contact(request):
    return HttpResponse('''
        <style>
            body {
                background-color: black;
                color: white; /* Set text color to white for better visibility */
            }
            h1 {
                color: red;
                text-align: center;
            }
            ul {
                list-style-type: none;
                margin: 0;
                padding: 0;
            }
            li {
                display: inline;
                margin-right: 20px;
            }
            a {
                text-decoration: none;
                color: white;
                font-weight: bold;
            }
        </style>
        <h1>This is Contact page</h1>
        <ul>
            <li><a href="/second_app/feedback/">Feedback</a></li>
            <li><a href="/second_app/course/">Course</a></li>
            <li><a href="/first_app/about/">About</a></li>
        </ul>
    ''')

# def about(request):
#     return HttpResponse("This is our about page")

def about(request):
    return HttpResponse('''
        <style>
            body {
                background-color: black;
                color: white; /* Set text color to white for better visibility */
            }
            h1 {
                color: red;
                text-align: center;
            }
            ul {
                list-style-type: none;
                margin: 0;
                padding: 0;
            }
            li {
                display: inline;
                margin-right: 20px;
            }
            a {
                text-decoration: none;
                color: white;
                font-weight: bold;
            }
        </style>
        <h1>This is About page</h1>
        <ul>
            <li><a href="/second_app/feedback/">Feedback</a></li>
            <li><a href="/first_app/contact/">Contact</a></li>
            <li><a href="/second_app/course/">Course</a></li>
        </ul>
    ''')
