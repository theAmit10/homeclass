from django.shortcuts import render, redirect
from django.contrib import messages, auth 
from django.contrib.auth.models import User 
from .models import Teachers


# Create your views here.
def register(request):
    if request.method == 'POST':
        # get the value of the form which use POST methods.
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email'] 
        phone = request.POST['phone']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check if password match
        if password == password2:
            # check username
            if Teachers.objects.filter(username=username).exists():
                messages.error(request, 'The Username is Taken, Try Another One.')
                return redirect('register')
            else:
                if Teachers.objects.filter(email=email).exists():
                    messages.error(request, 'The Email is being Used.')
                    return redirect('register')
                else:
                    # looks good if everything is correct than create user.
                    user = Teachers(username=username, password=password,
                    email=email, firstname=first_name, lastname= last_name , phone=phone, confirmPassword=password2 )
                    # login after register
                    # auth.login(request, user)
                    # messages.success(request, ' you are noe logged in')
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'you are now Registered')
                    return redirect('login')

        else:
            messages.error(request, 'Password Do Not Match.')
            return redirect('register')
    else:
        return render(request, 'Teachers/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

       # user = auth.authenticate(username=username, password=password )
        user = Teachers(username=username, password=password )

        #if user is not None:
            #auth.login(request,user)
        if(Teachers.objects.filter(username=username, password=password).exists()):
            messages.success(request, 'You are logged in')
            return redirect('classes')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
        
       
    else:
        return render(request, 'Teachers/login.html')

















