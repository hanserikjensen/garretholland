from flask import Flask, render_template, redirect, request, session, flash
import random, datetime, re

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

email_check = re.compile(r'[^@]+@[^@]+\.[^@]+')
passwd_check = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')

@app.route('/', methods=['POST', 'GET'])
def index():
    #set constants
    form_empty = False
    passwd_len = False
    passwd_match = False
    passwd_req = False
    # if submitted do the things
    if request.method == 'POST':
        #create a list from the form
        inputs = request.values
        #loop through each input and test conditionals
        for value in inputs:
            #check if inputs are empty
            if len(request.form[value]) == 0:
                form_empty = True
            #check if firstname and lastname have any ints
            if value == 'fname' or value == 'lname':
                if any (char.isdigit() for char in request.form[value]):
                    flash("Names can't have numbers in them, please input your name only.")
            #check if password and confirmed password, are at least 8 characters, has 1 upper, 1 lower, 1 number, and match
            if value == 'passwd' or value == 'confirm':
                if len(request.form[value]) < 8:
                    passwd_len = True
                if passwd_check.match(request.form[value]):
                    pass
                else:
                    passwd_req = True
                if request.form['passwd'] != request.form['confirm']:
                    passwd_match = True
            #check if email is a valid email
            if value == 'email':
                if email_check.match(request.form[value]):
                    pass
                else:
                    flash("Please input a valid e-mail address")

    #flash statements
    if form_empty == True:
        flash('All boxes must be filled in, check to be sure there are no empty boxes')
    if passwd_len == True:
        flash("Password must be at least 8 Characters")
    if passwd_match == True:
        flash("Password and Confirmation don't match")
    if passwd_req == True:
        flash("Password must contain one uppercase letter, one lowercase letter and one number")


    return render_template('index.html')

app.run(debug=True)
