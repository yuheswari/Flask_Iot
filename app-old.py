import math
from flask import Flask, render_template, request, redirect, url_for
import os
import math

app = Flask(__name__, template_folder="templates-old")
basename = '/iotcloud'

@app.route(basename + "/hello_world")
def hello_world():
    d = {
        "username": whoami().strip(),
        "env": "labs",
        "avatar": "https://yuheswari.me/images5.png"
    }
    return render_template('helloworld.html', data=d)

@app.route(basename+"/dashboard")
def dashboard():
   return render_template('dashboard.html', data={
      "title": "IoT Dashboard"
   })


@app.route('/')
def hello():
    return "<h1>Welcome to UKCREA</h1>"

@app.route('/whoami')
def whoami():
    return os.popen('whoami').read()

@app.route(basename + '/encode/<string>')  # encode the string ref http encoding
def echo(string):
    print(string)
    return string

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug=True)