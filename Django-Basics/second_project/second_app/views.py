from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def course(request):
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
        <h1>This is Course page</h1>
        <ul>
            <li><a href="/second_app/feedback/">Feedback</a></li>
            <li><a href="/first_app/contact/">Contact</a></li>
            <li><a href="/first_app/about/">About</a></li>
        </ul>
    ''')

def feedback(request):
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
        <h1>This is Feedback page</h1>
        <ul>
            <li><a href="/second_app/course/">Course</a></li>
            <li><a href="/first_app/contact/">Contact</a></li>
            <li><a href="/first_app/about/">About</a></li>
        </ul>
    ''')

