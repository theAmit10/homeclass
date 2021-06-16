from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Taclass

# Create your views here.
def classes(request):

    taclass = Taclass.objects.all()

    context = {
        'taclass' : taclass 
    }

    return render(request, 'taclass/classes.html', context)

def subject(request):

    taclass = Taclass.objects.all()
    

    content = {
        'taclass' : taclass
    }

    if request.method == 'POST':
        
        
        assignment = request.POST['filepond']
        assignmentTitle = request.POST['message']
        code = request.POST['subjectCode']
        #classcode = Taclass.objects.all().filter(classCode__iexact==code)
        
        
        subject = Taclass(assignment=assignment, assignmentTitle=assignmentTitle)
        subject.save()

        return render(request, 'taclass/subject.html', content)

    return render(request, 'taclass/subject.html', content)


def createclass(request):
    if request.method == 'POST':
        subject = request.POST['subject_name']
        classname = request.POST['class_name']
        classimage = request.POST['class_image']
        teachername = request.POST['teacher_name']
        section = request.POST['section']

        if Taclass.objects.filter(subject=subject).exists():
            messages.error(request, 'The Subject Name is Taken, Try Another One.')
            return redirect('createclass')
        else:
            if Taclass.objects.filter(classname=classname).exists():
                messages.error(request, 'The Class Name is being Used.')
                return redirect('createclass')
            else:
                user = Taclass(subject=subject, classname=classname, classimage=classimage, teachername=teachername, section=section,)
                user.save()
                messages.success(request, 'you are now Registered')
                return redirect('classes')

              
    else:
        return render(request, 'taclass/createclass.html')