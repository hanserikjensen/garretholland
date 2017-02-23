from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import User


def index(request):
    return render(request, 'index.html')


def success(request):
    context = request.session['context']

    return render(request, 'success.html', context)


def process(request):
    print ">>>>>>hit process<<<<<<<<<"
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

                return redirect('login_register:success')

            else:
                for err in data[1]:
                    messages.error(request, err)

        elif request.POST.get('login'):
            print ">>>>>>>>>>>>hit login in process<<<<<<<<<"

            data = User.objects.login(request.POST)
            print "data is---------->>>>>>", data

            if data[0] == True:
                print ">>>>>>>data[1] is: --------->>>>>>>>>", data[1]
                context = {
                    "name": data[1].firstname,
                    "logged_in": "Successfully logged in!",
                }

                request.session['context'] = context

                user = list(data)
                print "user[1] is ------>>>>>>>", user[1]
                user = User.objects.filter(firstname=user[1])
                print "user --------->>>>>>>>>>>>", user
                print "user.firstname is --->>>>>>>>", user[0].id
                request.session['user_id'] = user[0].id
                print "request.session[user_id] is ------>>>", request.session['user_id']

                print "user is--->>>>>>>>>>>", user

                return redirect('login_register:success')

            else:
                for err in data[1]:
                    messages.error(request, err)


        return redirect('login_register:index')

#login_register:success

def redirect(request):
    print ">>>>>>>>>>request is------->>>>>>>>>", request
    print "request.session[user_id] in redirect is ------>>>", request.session['user_id']
    # if request.GET:
    #     print "request.GET is ---------->>>>>>", request.GET
    #     return redirect('courses_app:index')

# def logout(request):
#     try:
#         del request.session['member_id']
#     except KeyError:
#         pass
#     return HttpResponse("You're logged out.")
