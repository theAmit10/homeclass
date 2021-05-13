from django.shortcuts import render
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