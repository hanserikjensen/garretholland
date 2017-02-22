from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import User


def index(request):
    return render(request, 'index.html')


def success(request):
    context = request.session['context']

    return render(request, 'success.html', context)


def process(request):
    if request.method == "POST":
        print ">>>>>>>>>request.POST-------->>>>>>>>>>", request.POST
        if request.POST.get('register'):
            print ">>>>>>>>hit register in process<<<<<<<<"

            data = User.objects.register(request.POST)

            if data[0] == True:

                context = {
                    "name": data[1].firstname,
                    "registered": "Successfully registered!",
                }
                # request.session['name'] = data[1].firstname
                request.session['context'] = context

                return redirect('/success')

            else:
                for err in data[1]:
                    messages.error(request, err)

        elif request.POST.get('login'):
            print ">>>>>>>>>>>>hit login in process<<<<<<<<<"

            data = User.objects.login(request.POST)

            if data[0] == True:
                context = {
                    "name": data[1].firstname,
                    "logged_in": "Successfully logged in!",
                }

                request.session['context'] = context

                return redirect('/success')

            else:
                for err in data[1]:
                    messages.error(request, err)


        return redirect('/')

# def logout(request):
#     try:
#         del request.session['member_id']
#     except KeyError:
#         pass
#     return HttpResponse("You're logged out.")
