from flask import Flask, render_template

# Import other necessary modules
from frontpage import *
from hostname2 import *
from QR import *
from Confirm import *
from generatereset import *
from adintegrity import *

app = Flask(__name__)

@app.route('/frontpage')
def frontpage():
    return render_template('frontpage.py')

@app.route('/hostname2')
def hostname2():
    return render_template('hostname2.py')

@app.route('/QR')
def qr():
    return render_template('qr.py')

@app.route('/Confirm/<username>')
def confirm(username):
    return f"User: {username}"

@app.route('/generatereset/<username>')
def generatereset(username):
    return f"User: {username}"

@app.route('/adintegrity/<username>')
def adintegrity(username):
    return f"User: {username}"

if __name__ == '__main__':
    app.run(debug=True)
