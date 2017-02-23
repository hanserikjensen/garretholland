from django.shortcuts import render, HttpResponse, redirect
from models import Course, Description, Comments

def index(request):
    context={
        'courses': Course.objects.all(),
        'description': Description.objects.all(),
        'comments': Comments.objects.all(),
    }

    return render(request, 'courses_app/index.html', context)


def create_course(request):
    #if request is POST create a course
    if request.method == "POST":
        Course.objects.create_course(request.POST['course'])
        Description.objects.add_description(request.POST['description'])

        return redirect('/')


def destroy_course(request, course_id):
    if request.method == "POST":
        for key in request.POST:
            if key == 'destroy':
                Course.objects.destroy_course(course_id)
                request.session['destroy'] = True

                return redirect('/')

            elif key == 'keep':
                return redirect('/')

    else:
        course = Course.objects.get(id=course_id)
        context = {
            'course': Course.objects.get(id=course_id)
        }

        return render(request, 'courses_app/destroy.html', context)


def create_comment(request, course_id):
    if request.method == "POST":
        course = Course.objects.get(id=course_id)
        Comments.objects.create_comment(request.POST['comment'], course)

        return redirect('/')
