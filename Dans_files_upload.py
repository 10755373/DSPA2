#  Code modified from https://medium.com/spatial-data-science/how-to-extract-gps-coordinates-from-images-in-python-e66e542af354
#  and https://www.youtube.com/watch?v=gLyaR3KPYt4, Accessed on 13-01-2022

import os
import pyrebase
import cv2
from PIL import Image
from exif import Image


def decimal_coords(gps_data, ref):
    """ Helper function to get the GPS coordinates from GPS meta data. """
    decimal_degrees = gps_data[0] + gps_data[1] / 60 + gps_data[2] / 3600
    if ref == "S" or ref == "W":
        decimal_degrees = -decimal_degrees
    return decimal_degrees


def upload_images_from_folder(folder, database, storage):
    """ Reads in all the images from a folder, extracts the longitude, latitude and datetime data and
        uploads it to the database.

        Argument:
            - folder:   string with the name of the image folder.
    """
    for filename in os.listdir(folder):
        img_path = os.path.join(folder, filename)

        # Checks if there is an image with that filename, if not continues to the next.
        with open(img_path, "rb") as src:
            img = Image(src)
        if img is None:
            continue

        # Checks if the image has exif data, otherwise prints message saying it does not.
        if img.has_exif:

            # Tries to get all the needed exif data, if it fails it prints a message.
            try:
                latitude = decimal_coords(img.gps_latitude, img.gps_latitude_ref)
                longitude = decimal_coords(img.gps_longitude, img.gps_longitude_ref)
                datetime = img.datetime

                # Prepares the spot on the database and the data to be uploaded.
                path_on_cloud = ("Images/" + filename)

                # Uploads the image to the store.
                store.child(path_on_cloud).put(img_path)
                database.child(path_on_cloud.replace(".jpg", ""))
                data = {"filename": filename,
                        "latitude": latitude,
                        "longitude": longitude,
                        "datetime": datetime}

                # Tries to update the database spot with that name if data is already there.
                try:
                    database.update(data)

                # If there is no data in that spot yet, it sets the data.
                except AttributeError:
                    database.set(data)
            except AttributeError:
                print('No Coordinates or Time')
        else:
            print('The Image has no EXIF information')


# Database connection setup.
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

upload_images_from_folder("all_cctv_data", db, store)
