from django.shortcuts import render, HttpResponse, redirect
from models import Course, Description, Comments
# Create your views here.

def index(request):
    context={
        'courses': Course.objects.all(),
        'description': Description.objects.all(),
    }

    return render(request, 'courses_app/index.html', context)


def create_course(request):
    print "hit !!!!!views.py create_course!!!!"
    #if request is POST create a course
    if request.method == "POST":
        Course.objects.create_course(request.POST['course'])
        Description.objects.add_description(request.POST['description'])
        print "!!!!request.POST['description'] is -------------->>>>>", request.POST['description']

        return redirect('/')


def destroy_course(request, course_id):
    print ">>>>!!!!reached destroy_course!!!<<<<"
    print ">>>>>>>this is course_id inside of destroy_course!!-->>>>>>", course_id

    if request.method == "POST":
        ##I can't get the logic to work here, the first if statement works when true, but when not true it fails, this is reversed from order I had them in
        if request.POST['keep']:
            return redirect('/')

        elif request.POST['destroy']:
                print ">>>>>hit destroy_course past POST<<<<<"
                print ">>>>>>>>COURSE ID IN destroy_course IN IF REQUEST.METHOD['DESTROY'] IS ------->>>>>>", course_id
                Course.objects.destroy_course(course_id)
                request.session['destroy'] = True
                return  redirect('/')

    else:
        course = Course.objects.get(id=course_id)
        print "course is", course
        context = {
            'course': Course.objects.get(id=course_id)
        }

        return render(request, 'courses_app/destroy.html', context)

def create_comment2(request, course_id):
    print ">>>>>>hit create_comment <<<<<<<"
    if request.method == "POST":
        #Comments.objects.create(comment = request.POST['comment'])
        Comments.objects.create_comment(request.POST['comment'], course_id)

        return redirect('/')



# def destroy(request, course_id):
#     print ">>>>!!!!reached destroy_course!!!<<<<"
#     if request.method == "POST":
#         print ">>>>>hit destroy_course past POST<<<<<"
#         Course.objects.destroy_course(course_id)
#         print ">>>>>>course_id is: ------->>>>", course_id
#
#         return render(request, 'courses_app/destroy.html')
