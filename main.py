from flask import Flask, render_template, request
from tinydb import TinyDB

#To run in windows 10:
# activate venv:    venv/scripts/activate
# set up environment variable:  set FLASK_APP=main.py
# optional debug:               set FLASK_DEBUG=1
# run the application           flask run


#Conditionally import the Neurosteer logging tool. This allows for SW 
# development without the EEG in use.
nl = False
creds =''
bluetooth =''
if (nl):
    import NeurosteerLogin as nlf
    [creds, bluetooth] = nlf.login()


app = Flask(__name__, static_url_path='/static')


@app.route("/")
def index():
    return ("You are in the placeholder index page")


@app.route("/iproxy")
def iproxy():
        return render_template("iproxy.html")





@app.route("/ns_logger", methods = ['POST'])
def logger():
    print(request.form['msg'])
    if (nl):
            nlf.logEvent(creds, bluetooth, request.form['msg'])
    return('',204)
