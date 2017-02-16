from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
import re
from datetime import datetime

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
    print "hit index in apps/views"


    return render(request, 'index.html')

def process(request):
    if request.method == 'POST':
        print request.POST
        print 'hit apps/email_registration/views.py process method'
        # change post info to session
        request.session['email'] = request.POST['email']
        # validate email
        if email_regex.match(request.session['email']):
            # get user info
            user = User.objects.create(email=request.session['email'])
            # set context to send to success template process is a check to determine which <p> to display
            context = {
                "users": User.objects.all(),
                "process": True
            }
            return render(request, 'success.html', context)
        # if not a valid email, redirect to /
        else:
            print "hit else statement in process, email not valid"
            # flash email is not valid
            messages.add_message(request, messages.ERROR, 'Email is not valid!')
            return redirect('/')

def delete_link(request, user_id):
    print user_id, '<<<-----------------got user_id'
    # find the user associated with the provided id
    user = User.objects.get(id=user_id)
    # get email from user
    request.session['email'] = user.email
    print request.session['email'], "<<<<<<<<<<<--------this is request.session['user']"
    # delete the user/email
    User.objects.filter(id=user_id).delete()
    # repopulate list of emails entered to render on success.html
    context = {
        "users": User.objects.all()
    }
    request.session['delete_link'] = True


    return render(request, 'success.html', context)
