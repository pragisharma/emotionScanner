from flask import Flask, render_template
app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return 'Hello World!'


@app.route('/')
def index():
    ## /Users/pragya/Desktop/emotionScanner/templates
    return render_template('file_upload.html')







# other stuff from last time >> 

# import os 
# from flask import Flask, render_template, request, redirect, send_file,url_for
# from flask_sqlalchemy import SQLAlchemy
# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return 'Hello World!'


