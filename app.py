from flask import Flask, redirect, url_for, request, render_template
import json
import os
import math

app = Flask(__name__)
basename = '/iotcloud'

@app.route(basename + "/hello_world")
def hello_world():
    d = {
        "username": whoami().strip(),
        "env": "labs",
        "avatar": "https://yuheswari.me/images5.png"
    }
    return render_template('helloworld.html', data=d)


@app.route(basename + "/dashboard")
def dashboard():
    return render_template('dashboard.html', data={
        "title":"IOT Dashboard"
    })

@app.route('/')
def hello():
    return "<h1>Welcome to UKCREA</h1>"

@app.route('/whoami')
def whoami():
    return os.popen('whoami').read()

@app.route(basename + '/encode/<string>')  # encode the string ref http encoding
def echo(string):
   return string  # Ensure the function returns a valid response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug=True)