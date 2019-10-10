from flask import Flask, render_template, request
from tinydb import TinyDB

#To run in windows 10:
# activate venv:    venv/scripts/activate
# set up environment variable:  set FLASK_APP=main.py
# optional debug:               set FLASK_DEBUG=1
# run the application           flask run


#Conditionally import the Neurosteer logging tool. This allows for SW 
# development without the EEG in use.
nl = True
creds =''
bluetooth =''
if (nl):
    import NeurosteerLogin as nlf
    [creds, bluetooth] = nlf.login()


app = Flask(__name__, static_url_path='/static')




@app.route("/")
def index():
    return render_template("index.html")


@app.route("/read")
def readview():
    return render_template("read.html")

@app.route("/nothing")
def nothingview():
    return render_template("nothing.html")

@app.route("/game")
def gameview():
    return render_template("game.html")

@app.route("/video")
def videoview():
    return render_template("video.html", videosrc="\static\Wallace.And.Gromit.In.A.Close.Shave.1995.720p.BluRay.H264.AAC-RARBG.mp4")

@app.route("/music")
def musicview():
    return render_template("music.html", videosrc="\static\Wallace.And.Gromit.In.A.Close.Shave.1995.720p.BluRay.H264.AAC-RARBG.mp4")


@app.route("/iproxy")
def iproxy():
    return render_template("iproxy.html")


@app.route("/iframetest")
def iframetest():
    return render_template("iframetest.html")




@app.route("/ns_logger", methods = ['POST'])
def logger():
    print(request.form['msg'])
    if (nl):
            nlf.logEvent(creds, bluetooth, request.form['msg'])
    return('',204)
