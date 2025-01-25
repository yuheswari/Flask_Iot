from flask import Flask, redirect, url_for, request, render_template,session
import json
import os
import math
from src import get_config
from src.User import User

basename = get_config("basename")
app = Flask(__name__, static_folder='assets', static_url_path=basename)
app.secret_key=get_config("secret_key")

@app.route(basename+"/dashboard")
def dashboard():
   return render_template('dashboard.html',session=session)


@app.route(basename+"/auth", methods=['POST'])
def authenticate():
   if session.get('authenticated'):#todo need more validation like expiry 
      return{
        
            "message":"Already authenticated",
            "authenticated":True
         
      },202
   else:
      if 'username' in request.form and 'password' in request.form:
         username = request.form['username']
         password = request.form['password']
         try:
            User.login(username,password)
            print("Login success")
            return {
                "message":"successfully authenticated",
                "authenticated":True
            },200
            
         except Exception as e:
            print("Login failed",e)
            return {
                "message":e,
                "authenticated":False
            },401
      else:
         return{
            "message":"Not enough parameters",
            "authenticated":False
         },400
   



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug=True)