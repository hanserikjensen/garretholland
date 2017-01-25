from flask import Flask, render_template, redirect, request, session, flash
import random, datetime

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/process_money', methods=['POST'])
def process():
    # print session['gold']
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    time = str(time)

    if request.form['building'] == 'farm':
        num = random.randrange(10, 20)
        session['gold'] += num
        session['statement'] = "Earned " + str(num) + " golds from the farm!  " + time
        print session['statement']
    if request.form['building'] == 'cave':
        session['gold'] += random.randrange(5, 10)
    if request.form['building'] == 'house':
        session['gold'] += random.randrange(2, 5)
    if request.form['building'] == 'casino':
        session['gold'] += random.randrange(-50, 50)


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
