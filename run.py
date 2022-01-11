#Uploading page adapted from https://github.com/hemanth-nag/Camera_Flask_App/blob/main/camera_flask_app.py  
# and https://roytuts.com/upload-and-display-image-using-python-flask/, accesed 2022/07/01

from flask import Flask, render_template, Response, request,flash, redirect, url_for
import cv2
import datetime
import os
import geocoder
from metadata import PNG_to_JPG,metadata 
import urllib.request
from werkzeug.utils import secure_filename
import requests



# Upload code
# Saving pics from file
#ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

#def allowed_file(filename):
#	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#make shots directory to save pics
global capture,switch 
capture=0
switch=0
# get the coordinates of ip address
g = geocoder.ip('me')
#set uploading folder where the files are needed 
UPLOAD_FOLDER = r'DS_MASTER\DSP\DSPA2-main\static\uploads'


URL = "https://geocoder.api.here.com/6.2/geocode.json"
location = input("Enter the location here: ")
app_ID = 'LVzP8znwHiItQlnZsd3g'
app_CODE = 'ufbceoJhaG-H270WOS1rww'
PARAMS = {'app_id':app_ID,'app_code':app_CODE,'searchtext':location} 

# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 
data = r.json()

latitude = data['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Latitude']
longitude = data['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Longitude']


app = Flask(__name__)

#Uploading code
#app.secret_key = "secret key"
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
#Opens camara
camera = cv2.VideoCapture(1)


# Defines the routes to the webpages.
@app.route("/")
@app.route("/index.html")
def home():
    return render_template("index.html")

@app.route("/gallery.html")
def gallery():
    return render_template("gallery.html")

@app.route("/map.html")
def map():
    # return render_template("map.html")
	return render_template('map.html',app_ID=app_ID,app_CODE=app_CODE,latitude=latitude,longitude=longitude)


#Uploaging page code
# generate frame by frame from camera
def gen_frames():  
    global out, capture,rec_frame
    while True:
        success, frame = camera.read() 
        if success: 
            if(capture):
                #Taking pic from webcam 
                capture=0
                now = datetime.datetime.now()
                #square pic
		height,width = frame.shape[0],frame.shape[1]
                frame = frame[round(height*0.25):round(height*0.25)+ round(width*0.35), round(width*0.40):round(width*0.40)+ round(width*0.35)]
		
                p = os.path.sep.join([UPLOAD_FOLDER, "camshot_{}.png".format(str(now).replace(":",''))])
                cv2.imwrite(p, frame)
                p_new = os.path.sep.join([UPLOAD_FOLDER, "camshot_new_{}.jpg".format(str(now).replace(":",''))])
                p_metadata = os.path.sep.join([UPLOAD_FOLDER, "camshot_meta_{}.jpg".format(str(now).replace(":",''))])
                PNG_to_JPG(p,p_new)
                metadata(p_new,g.latlng[0],g.latlng[1],p_metadata)
                
            try:
                ret, buffer = cv2.imencode('.jpg', cv2.flip(frame,1))
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            except Exception as e:
                pass
                
        else:
            pass

@app.route("/upload.html")
def upload():
    return render_template("upload.html")
# Displays the camara 
@app.route("/video_feed")
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
# Buttons functionality
@app.route("/requests",methods=['POST','GET'])
def tasks():
    global switch,camera
    if request.method == 'POST':
        if request.form.get('click') == 'Capture':
            global capture
            capture=1

        elif  request.form.get('stop') == 'Stop/Start':
      
            if(switch==1):
                switch=0
                camera.release()
                  
            else:
                camera = cv2.VideoCapture(0)
                switch=1
            
                 
    elif request.method=='GET':
        return render_template('upload.html')
    return render_template('upload.html')


@app.route("/ethics_paper.html")
def ethics_paper():
    return render_template("ethics_paper.html")

if __name__ == "__main__":
    app.run(debug=True)
#closes camara
camera.release()
