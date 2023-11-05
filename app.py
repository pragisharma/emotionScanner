import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace
from config import Config
from skimage import io

from flask import Flask, render_template, request, send_from_directory

from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

app.config.from_object(Config)

@app.route('/')
def index():
    ## /Users/pragya/Desktop/emotionScanner/templates
    return render_template('file_upload.html')

@app.route('/storeimg', methods=['POST'])
def store_img():
    img_file = request.files['imgforminput']
    # get file from HTML form
    if img_file.filename == '':
        return '<h1>NO FILE UPLOADED</h1>'
    
    filename = secure_filename(img_file.filename)
    file_loc = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    img_file.save(file_loc)
    eopt = process(file_loc)
    
    if(eopt == 'happy') :
        m = "did u instictively smile bc of the photo or are you truly happy?"
    elif(eopt == 'angry') :
        m = "hey hey, try taking a few deep breaths"
    elif(eopt == 'sad') :
        m = "its okay to feel down, try talking it out with someone"
    elif(eopt == 'disgust') :
        m = "ew, disgusting, did u eat peas?"
    elif(eopt == 'surprise') :
        m = "SURPRISE WHAT HAPPENED"
    elif(eopt == 'fear') :
        m = "BOO, what's so scary..?"
    elif(eopt == 'neutral') :
        m = "ok ._."
    else :
        m = "ur feeling a mix of emotions?"
    
    # return render_template('output.html', message=m)  
    # return render_template('output.html', emotion_output=eopt)   
    return render_template('output.html', message=m)   

def process(location):
    img = cv2.imread(location)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    detector=cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
    faces = detector.detectMultiScale(gray, 1.1, 4)
    # look into how necessary the bounding-box part is
    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    predictions =  DeepFace.analyze(img)
    predictions = predictions[0]
    print("PREDICTIONS ARE:")
    print(predictions)
    dominant_emotion = predictions['dominant_emotion']
    return dominant_emotion

# def process(loc):
#     img = io.imread(loc)
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faceCascade = cv2.CascadeClassifier('haarcascades_frontalface_default.xml')
#     faces = faceCascade.detectMultiScale(gray, 1.1, 4)

#     for(x, y, w, h) in faces:
#         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

#     predictions =  DeepFace.analyze(img)
#     predictions = predictions[0]
#     print(predictions)
#     dominant_emotion = predictions['dominant_emotion']
#     return dominant_emotion





# other stuff from last time >> 

# import os 
# from flask import Flask, render_template, request, redirect, send_file,url_for
# from flask_sqlalchemy import SQLAlchemy
# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return 'Hello World!'


