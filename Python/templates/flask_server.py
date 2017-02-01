from flask import Flask, render_template, redirect, request, session, flash
import random, datetime

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
    return render_template('index.html')
