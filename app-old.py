from flask import Flask
from flask import Flask, redirect, url_for, request,render_template
import json
import os
import math
from src import check
from src.User import User
app = Flask(__name__)
basename='/iotcloud'

check()

@app.route(basename+"/hello_world")
def hello_world():
   d={
      "username":whoami().strip(),
      "env":"labs",
      "avatar":"https://yuheswari.me/images5.png"   
      }
   return render_template('helloworld.html',data=d)


@app.route('/')
def hello():
   return "<h1>Welcome to UKCREA</h1>"

@app.route('/whoami')
def whoami():
   return os.popen('whoami').read()

@app.route('/cpuinfo')
def cpuinfo():
   if isadmin == "yes madam proceeed!!!":
      return redirect(url_for('error', errorcode=1000))
   else:
      return "<pre>"+ os.popen('cat /proc/cpuinfo').read()+"</pre>"
   
@app.route(basename+"/error/<int:errorcode>")
def error(errorcode):
   if (errorcode == 1000):
      return "This app is running as root user which is dangerous!!"
   elif (errorcode == 1001):
      return "some other error!!"
   else:
      return "Unknown error!!"
   
@app.route(basename+'/echo')
def echo_help():
   return "Plese write some /echo/{some string}"

@app.route(basename+'/echo/<string>')
def echo(string):
   return string

@app.route(basename+'/isadmin',methods=['GET','POST'])
def isadmin():
   if whoami().strip()== "root":                  
      return "yes madam proceeed!!!"
   else:
      return "no madm sorrry next tym!!"

   
@app.route(basename+'/pow/<int:a>/<int:b>')
def power(a,b):
   return "Pow of {},{}: {}".format(a,b ,math.pow(a,b))


@app.route(basename+"/math/sqrt",methods=['GET','POST'])
def math_sqrt():
   return json.dumps(request.form)

app.add_url_rule(basename+'/whoami', 'whoami', whoami)
app.add_url_rule(basename+'/cpuinfo', 'cpuinfo', cpuinfo)
if __name__ == '__main__':
   app.run(host='0.0.0.0',port=7000,debug=True)