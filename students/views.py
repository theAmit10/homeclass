from django.shortcuts import render

def register(request):
    return render(request, 'students/register.html')

def login(request):
    return render(request, 'students/login.html')
