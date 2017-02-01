from flask import Flask, render_template, redirect, request, session, flash
# If you don't use it, don't import it ^ (flash)
import random, datetime

'''
This doesn't work.  Somewhere in here, you're getting a KeyError: 'gold' (The key 'gold' does not exist within a dictionary-like construct).  - N.T.
'''

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

#Watch your newline usage, everything being crammed together makes it very difficult to read.
@app.route('/')
def index(): #Add a description here for your routes, it'll help keep things organized.  Ex: Displays main-page.
    return render_template('index.html')


@app.route('/process_money', methods=['POST'])
def process(): #Description: Handles POST submissions on-click to update our gold count.

    # print session['gold']
	# ^ This should've given you your key error, solid attempt to troubleshoot.
	# What is currently stored in session['gold']?

    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #print type(time) See Notes below and uncomment this line to verify.
    #time = str(time) No need for this.
	# ^ strftime stands for String From Time [Object].  No need to cast type to a string here, since
	# strftime is a method that returns a string-type.

    if request.form['building'] == 'farm':
		#Let's examine this code block thoroughly, the rest have the same issue.
        num = random.randrange(10, 20) #This is okay.

		#At runtime, we're encountering the issue of 'gold' not being in the dictionary...So, this line in particular seems very off.
        session['gold'] += num

		# += is shorthand.  Let's write this out properly.
		# session['gold'] = session['gold'] + num
		# Chronologically, the steps taken by the interpreter are as follows.
		# 1. Evaluate session['gold'] (Right-hand side of the assignment operator)
		# 2. Evaluate num
		# 3. Add the values together
		# 4. Store the result into session['gold'] (Left-hand side of the assignment operator)

		#In step 1, session['gold'] is not previously holding a value at any point of this code.  Unlike Javascript, Python does not automatically declare variable values to "undefined" or any other value.
		#In this case, it throws a KeyError, because there is no value associated with the key 'gold' when it tries to evaluate it.
		# ^ This is the issue the interpreter is throwing.  All the other ifs below this have the same error.

		#The two statements below this are A-okay.
        session['statement'] = "Earned " + str(num) + " golds from the farm!  " + time
        print session['statement']

    if request.form['building'] == 'cave':
        session['gold'] += random.randrange(5, 10) #See above comments.
    if request.form['building'] == 'house':
        session['gold'] += random.randrange(2, 5) #See above comments.
    if request.form['building'] == 'casino':
        session['gold'] += random.randrange(-50, 50) #See above comments.
	#These ifs above ^ are mutually exclusive (You can only press one of the four buttons at a time; logical inverse: You cannot press two or more buttons at the same time).  Therefore, they should be in an if/elif chain, instead of multiple ifs.


	#I do not know what any of this commented stuff below is for.  I presume it was for troubleshooting the issue documented above or perhaps some un-deleted code [Good, don't ever delete while learning].
        # return redirect('/')
        # if request.form.input['value'] == 'farm':
        #     session['gold'] += random.randrange(10, 20)
        # print session['gold']


    # session['cave'] = request.form['action']
    # session['house'] = request.form['action']
    # session['casino'] = request.form['action']

    return redirect('/')
# @app.route('/')
# def show_user():
#     return render_template('user.html', name='Jay', email='kpatel@codingdojo.com')

app.run(debug=True)
# WERKZEUG_DEBUG_PIN = off
