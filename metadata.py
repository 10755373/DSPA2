
from PIL import Image as Im
import math
from exif import Image
import os 
import datetime, time


def PNG_to_JPG(filename,filename_new):
    #transfrom PNG to JPG to edit metadata
    im1 = Im.open(filename)
    im1.save(filename_new)
    os.remove(filename)


def DD2DMS(latlon):
    # Transform decimal coordinates to degree coorsinates fro GPS metadata
    frac, whole = math.modf(latlon)
    frac_1,whole_1 = math.modf(frac*60)
    min = whole_1
    sec = frac_1*60
    return (whole,min,sec)
def ref(lat, lon):
    #Get GPS references
    if lat >= 0:
        reflat = 'N'
    if lat < 0:
        reflat = 'S'
    if lon >= 0:
        reflon = 'E'
    if lon < 0:
        reflon = 'W'
    return(reflat,reflon)



def metadata (filename_path,lat,lon, new_name_path):
    # Get N,S,W,E
    ref_latlon = ref(lat,lon)
    #open image
    with open(filename_path, 'rb') as image_file:
        my_image = Image(image_file)

    #Add metadata lon lat date
    my_image.gps_longitude = DD2DMS(lon)
    my_image.gps_longitude_ref = ref_latlon[1]
    my_image.gps_latitude = DD2DMS(lat)
    my_image.gps_latitude_ref = ref_latlon[0]
    now = datetime.datetime.now()
    now = now.strftime('%Y:%m:%d %H:%M:%S')
    my_image.datetime = str(now)

    #create new file with metadata
    with open(new_name_path , 'wb') as new_image_file:
        new_image_file.write(my_image.get_file())
    # delete old file without metadat
    os.remove(filename_path)    

