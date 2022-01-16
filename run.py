#Uploading page adapted from https://github.com/hemanth-nag/Camera_Flask_App/blob/main/camera_flask_app.py  
# and https://roytuts.com/upload-and-display-image-using-python-flask/, accesed 2022/07/01

from flask import Flask, render_template, Response, request, json
import cv2
import datetime
import os
import geocoder
from metadata import PNG_to_JPG,metadata
import requests

import torch
from torchvision import transforms
import albumentations as A 
from albumentations.pytorch import ToTensorV2
from PIL import Image
import numpy

import pyrebase

# Upload code
# Saving pics from file
#ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

#def allowed_file(filename):
#	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#make shots directory to save pics
global capture,switch,model,transform,device,db,store 
capture=0
switch=0

# get the coordinates of ip address
g = geocoder.ip('me')

#set uploading folder where the files are needed 
UPLOAD_FOLDER = r'.\static\uploads'


URL = "https://geocoder.api.here.com/6.2/geocode.json"
app_ID = 'LVzP8znwHiItQlnZsd3g'
app_CODE = 'ufbceoJhaG-H270WOS1rww'
PARAMS = {'app_id':app_ID,'app_code':app_CODE,'searchtext':"amsterdam"}

# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 
data = r.json()

#latitude = data['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Latitude']
#longitude = data['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Longitude']

config = {
    "apiKey": "AIzaSyDsgkvnYUtXSDQbG6VHQ1wsA85OgMl35dg",
    "authDomain": "dspa2-89403.firebaseapp.com",
    "databaseURL": "https://dspa2-89403-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "dspa2-89403",
    "storageBucket": "dspa2-89403.appspot.com",
    "messagingSenderId": "1067069276652",
    "appId": "1:1067069276652:web:a7905bfd04c842886780c9",
    "measurementId": "G-9LFKZ5YGHG",
    "serviceAccount": "serviceAccountKey.json"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
store = firebase.storage()

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model = torch.load('./models/resnet/resnet18_pretrained32.pth')
model.eval()
transform = A.Compose(
    [
        A.Resize(32,32),
        A.Normalize(
            mean=(0,0,0),
            std =(1,1,1),
            max_pixel_value=225,
        p=1),
        
        ToTensorV2(),
    ]
)

app = Flask(__name__)

#Uploading code
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
#Opens camara
#camera = cv2.VideoCapture(1)


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
'''
def gen_frames():  
    global out, capture,rec_frame
    while True:
        success, frame = camera.read() 
        if success: 
            if(capture):
                #Taking pic from webcam 
                capture=0
                now = datetime.datetime.now()
                height,width = frame.shape[0],frame.shape[1]
                frame = frame[round(height*0.25):round(height*0.25)+ round(width*0.35), round(width*0.40):round(width*0.40)+ round(width*0.35)]
                img = transform(image=numpy.array(frame))['image'].to(device).unsqueeze(0)
                if get_prediction(img, model)[0].item() == 0:
    
                    p = os.path.sep.join([UPLOAD_FOLDER, "camshot_{}.png".format(str(now).replace(":",''))])
                    cv2.imwrite(p, frame)
                    p_new = os.path.sep.join([UPLOAD_FOLDER, "camshot_new_{}.jpg".format(str(now).replace(":",''))])
                    p_metadata = os.path.sep.join([UPLOAD_FOLDER, "camshot_meta_{}.jpg".format(str(now).replace(":",''))])
                    PNG_to_JPG(p,p_new)
                    metadata(p_new,g.latlng[0],g.latlng[1],p_metadata)
                else:
                    pass
            height,width = frame.shape[0],frame.shape[1]
            color = (0,0,0)
            thickness = 3

            frame = cv2.line(frame,(round(width*0.40),round(height*0.25)),(round(width*0.40)+ round(width*0.35),round(height*0.25)),color,thickness) 
            frame = cv2.line(frame,(round(width*0.40),round(height*0.25)+ round(width*0.35)),(round(width*0.40)+ round(width*0.35),round(height*0.25)+ round(width*0.35)),color,thickness) 
            frame = cv2.line(frame,(round(width*0.40),round(height*0.25)),(round(width*0.40),round(height*0.25)+ round(width*0.35)),color,thickness) 
            frame = cv2.line(frame,(round(width*0.40)+ round(width*0.35),round(height*0.25)),(round(width*0.40)+ round(width*0.35),round(height*0.25)+ round(width*0.35)) ,color,thickness) 

            ret, buffer = cv2.imencode('.jpg', cv2.flip(frame,1))
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
           
                
        else:
            pass


'''
    
@app.route("/upload.html")
def upload():
    return render_template("upload.html")

@app.route('/photo', methods=['GET', 'POST'])
def photo():
    if request.method == 'POST':
         # it raise error when there is no `snap` in form
        fs = None
        fs = request.files.get('snap')
        
        print(type(fs))
        if fs: 
            print('FileStorage:', fs)
            print('filename:', fs.filename)
            b_image = Image.open(fs.stream).convert('RGB')
            img = transform(image=numpy.array(b_image))['image'].to(device).unsqueeze(0)
            print(get_prediction(img, model)[0].item())
            if get_prediction(img, model)[0].item() == 0:
                now = str(datetime.datetime.now())
                lat = latitude
                lon = longitude
                filename = "camshot_{}.jpg".format(now.replace(":",'').replace(' ','_').replace('.','-'))
                print(now, lat, lon, filename)
                
                b_image.save(filename)
                
                path_on_cloud = ("Images/" + filename)
                
                
                # Uploads the image to the store.
                store.child(path_on_cloud).put(filename)
                db.child(path_on_cloud.replace(".jpg", ""))
                data = {"filename": filename,
                        "latitude": latitude,
                        "longitude": longitude,
                        "datetime": now}
                
                os.remove(filename)
                
                # Tries to update the database spot with that name if data is already there.
                try:
                    db.update(data)

                # If there is no data in that spot yet, it sets the data.
                except AttributeError:
                    db.set(data)
                response='Got Snap! Your CCTV Sign has been saved.'
            else:
                response='No CCTV Sign has been detected! Please, Try Again.'
        else: 
            response='You forgot Snap!'
        return json.jsonify({ 
            'response': response 
        }) 
        

def get_prediction(image, model):
    with torch.no_grad():
        output = model(image)
        # the class with the highest energy is what we choose as prediction
        _, predicted = torch.max(output.data, 1)
        return predicted
    
@app.route('/location', methods=['POST'])
def location():
    global latitude, longitude
    latitude, longitude = None, None
    latitude = request.json.get('latitude')
    longitude = request.json.get('longitude')
    print(latitude, longitude)
    return 'Location Sent!'

def to_database():
    pass
'''
# Displays the camara 
@app.route("/video_feed")
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
# Buttons functionality

@app.route("/requests",methods=['POST','GET'])
def tasks():
    global switch,camera
    if request.method == 'POST':
        if request.form.get('click') == 'Take CCTV':
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
'''

@app.route("/ethics_paper.html")
def ethics_paper():
    return render_template("ethics_paper.html")

if __name__ == "__main__":
    app.run(debug=True)

#closes camara
#camera.release()
