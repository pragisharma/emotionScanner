import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace
from config import Config

from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return 'Hello World!'


## @app.route('/submit', methods-['POST'])


@app.route('/')
def index():
    ## /Users/pragya/Desktop/emotionScanner/templates
    return render_template('file_upload.html')


def process(location):
    img = cv2.imread(location)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faceCascade = cv2.CascadeClassifier('haarcascades_frontalface_default.xml')
    faces = faceCascade.detectMultiScale(gray, 1.1, 4)

    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    predictions =  DeepFace.analyze(img)
    predictions = predictions[0]
    print(predictions)
    dominant_emotion = predictions['dominant_emotion']
    return dominant_emotion





# other stuff from last time >> 

# import os 
# from flask import Flask, render_template, request, redirect, send_file,url_for
# from flask_sqlalchemy import SQLAlchemy
# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return 'Hello World!'


