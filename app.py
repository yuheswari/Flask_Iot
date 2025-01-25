from flask import Flask, redirect, url_for, request, render_template
import json
import os
import math
from src import get_config
basename = get_config("basename")
app = Flask(__name__, static_folder='assets', static_url_path=basename)


@app.route(basename+"/dashboard")
def dashboard():
   session ={
       "authenticated":True,
       "username":"yuheswari2525"
   }
   return render_template('dashboard.html',session=session)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug=True)