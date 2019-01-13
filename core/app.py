from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('boneapp.html')

@app.route('/madGab')
def result():
    return render_template('spellTest.html')

# @app.route('/madGab')
# def madGab():
#     return render_template('boneapp.html')
