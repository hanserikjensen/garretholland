from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import User


def index(request):
    return render(request, 'index.html')


def success(request):
    return render(request, 'success.html')


def process(request):
    if request.method == "POST":
        print ">>>>>>>>>request.POST-------->>>>>>>>>>", request.POST
        if request.POST.get('register'):
            print ">>>>>>>>hit register in process<<<<<<<<"

            data = User.objects.register(request.POST)

            if data[0] == True:
                request.session['name'] = data[1].firstname
                request.session['register'] = True

                return redirect('/success')

            else:
                for err in data[1]:
                    messages.error(request, err)

        if request.POST.get('login'):
            print ">>>>>>>>>>>>hit login in process<<<<<<<<<"

            data = User.objects.login(request.POST)

            if data[0] == True:
                request.session['name'] = data[1].firstname
                request.session['login'] = True

                return redirect('/success')

            else:
                for err in data[1]:
                    messages.error(request, err)




        return redirect('/')






        if request.POST.get('login'):
            print ">>>>>>>>hit login in process<<<<<<<<<<"
