from django.shortcuts import render, redirect, HttpResponse

def index(request):
    print "hit survey_form_app/views.py index"
    # return render(request, 'survey_form_app/index.html')
    return render(request, 'index.html')

def survey(request):
    print "hit survey_form_app/views.py submit"

    if request.method == "POST":
        if request.POST['submit']:
            request.session['count'] = request.session['count'] + 1

        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['locations']
        request.session['language'] = request.POST['languages']
        request.session['comment'] = request.POST['comment']


        return  redirect('/result')

def result(request):
    print "hit survey_form_app/views.py result"
    return render (request, 'survey_form_app/result.html')
