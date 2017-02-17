from django.shortcuts import render, HttpResponse, redirect
from models import Course, Description
# Create your views here.

def index(request):
    context={
        'courses': Course.objects.all(),
        'description': Description.objects.all(),
    }
    return render(request, 'courses_app/index.html', context)

def create_course(request):
    print "hit !!!!!views.py create_course!!!!"
    if request.method == "POST":
        name = request.POST['course']
        Course.objects.create_course(name)
        description = request.POST['description']
        Description.objects.add_description(description)
        print "!!!!description is -------------->>>>>", description

        return redirect('/')


def delete_course(reuqest):
    pass
