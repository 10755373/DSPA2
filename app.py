# Uploading page adapted from https://github.com/hemanth-nag/Camera_Flask_App/blob/main/camera_flask_app.py
# and https://roytuts.com/upload-and-display-image-using-python-flask/, accesed 2022/07/01

from flask import Flask, render_template, request
import datetime
import os
import geocoder
import requests

import torch
import albumentations as A
from albumentations.pytorch import ToTensorV2
from PIL import Image
import numpy

import pyrebase

# get the coordinates of ip address
g = geocoder.ip('me')

URL = "https://geocoder.api.here.com/6.2/geocode.json"
app_ID = 'LVzP8znwHiItQlnZsd3g'
app_CODE = 'ufbceoJhaG-H270WOS1rww'
PARAMS = {'app_id': app_ID, 'app_code': app_CODE, 'searchtext': "amsterdam"}

# sending get request and saving the response as response object
r = requests.get(url=URL, params=PARAMS)
data = r.json()

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
        A.Resize(32, 32),
        A.Normalize(
            mean=(0, 0, 0),
            std=(1, 1, 1),
            max_pixel_value=225,
            p=1),

        ToTensorV2(),
    ]
)

app = Flask(__name__)


# Defines the routes to the webpages.

# If index is loaded, set info message to true
@app.route("/")
def index():
    # return render_template("map.html")
    return render_template('map.html', infomessage=True, app_ID=app_ID, app_CODE=app_CODE)

# If map is loaded not as index, set info message to fasle
@app.route("/map.html")
def map():
    # return render_template("map.html")
    return render_template('map.html', infomessage=False, app_ID=app_ID, app_CODE=app_CODE)


@app.route("/info.html")
def home():
    return render_template("info.html")


@app.route("/gallery.html")
def gallery():
    return render_template("gallery.html")


@app.route("/upload.html")
def upload():
    return render_template("upload.html")


@app.route('/photo', methods=['GET', 'POST'])
def photo():
    if request.method == 'POST':

        # it raise error when there is no `snap` in form
        fs = request.files.get('snap')
        latitude = request.form.get('lat')
        longitude = request.form.get('lon')
        if fs:
            try:
                print('FileStorage:', fs)
                print('filename:', fs.filename)
                b_image = Image.open(fs.stream).convert('RGB')
                img = transform(image=numpy.array(b_image))['image'].to(device).unsqueeze(0)
                print(get_prediction(img, model)[0].item())
                if get_prediction(img, model)[0].item() == 0:
                    now = str(datetime.datetime.now())
                    filename = "camshot_{}.jpg".format(now.replace(":", '').replace(' ', '_').replace('.', '-'))
                    print(now, float(latitude), float(longitude), filename)

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
                    return '0'
                else:
                    return 'No CCTV sign detected.'
            except:
                return 'Location undefined.'
        else:
            return 'Something went wrong. Please, try again.'


def get_prediction(image, model):
    with torch.no_grad():
        output = model(image)

        # the class with the highest energy is what we choose as prediction
        _, predicted = torch.max(output.data, 1)
        return predicted


@app.route("/ethics_paper.html")
def ethics_paper():
    return render_template("ethics_paper.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
    # app.run(debug=True)
