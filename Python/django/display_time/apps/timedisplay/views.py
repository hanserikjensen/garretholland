from django.shortcuts import render, HttpResponse
import datetime

def index(request):
    print "this is views.py in main/apps/timedisplay"
    context = {
        "displaytime": datetime.datetime.now()
    }
    return render(request,'timedisplay/index.html', context)
