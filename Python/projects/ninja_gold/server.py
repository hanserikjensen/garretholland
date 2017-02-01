from flask import Flask, render_template, redirect, request, session, flash
import random, datetime

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/process_money', methods=['POST'])
def process():

    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    time = str(time)

    if request.form['building'] == 'farm':
        num = random.randrange(10, 20)
        session['gold'] += num
        session['statement'] = "Earned " + str(num) + " golds from the farm!  " + time
        session['activities'].append(session['statement'])
        print session['activities']
    if request.form['building'] == 'cave':
        num = random.randrange(5, 10)
        session['gold'] += num
        session['statement'] = "Earned " + str(num) + " golds from the cave!  " + time
        session['activities'].append(session['statement'])
    if request.form['building'] == 'house':
        num = random.randrange(2, 5)
        session['gold'] += num
        session['statement'] = "Earned " + str(num) + " golds from the house!  " + time
        session['activities'].append(session['statement'])
    if request.form['building'] == 'casino':
        num = random.randrange(-50, 50)
        session['gold'] += num
        if num > 0:
            session['statement'] = "Earned " + str(num) + " golds from the casino!  " + time
            session['activities'].append(session['statement'])
        elif num < 0:
            session['statement'] = "Entered a Casino and lost " + str(num) + " golds... Ouch!  " + time
            session['activities'].append(session['statement'])

    return redirect('/')


app.run(debug=True)
