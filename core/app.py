#!/usr/bin/python3
from flask import Flask, render_template, request
import phraseConverter
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('boneapp.html')

@app.route('/madGab')
def result():
    return render_template('spellTest.html')

@app.route('/getPhrase')
def res():
	phrase = request.args.get('phrase')
	return phraseConverter.phraseConvert(phrase)
# @app.route('/madGab')
# def madGab():
#     return render_template('boneapp.html')
