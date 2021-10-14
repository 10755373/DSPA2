# https://stackoverflow.com/questions/62067609/how-to-augment-all-the-images-in-a-folder-using-tensorflow
# Keras is not working for me; I thought it could only run on python2.7, but didn't work. Then used several other ptyhon version,
# without succes. Keras is uploaded in Anaconde and I'm using the right environment, so I don't know why it's not working.
# anyways, looks promissing.

import keras
import cv2
import os
import glob
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
datagen = ImageDataGenerator(rotation_range =15, 
                         width_shift_range = 0.2, 
                         height_shift_range = 0.2,  
                         rescale=1./255, 
                         shear_range=0.2, 
                         zoom_range=0.2, 
                         horizontal_flip = True, 
                         fill_mode = 'nearest', 
                         data_format='channels_last', 
                         brightness_range=[0.5, 1.5]) 


img_dir = "folder-name" # Enter Directory of all images 
data_path = os.path.join(img_dir,'*g')
files = glob.glob(data_path)
data = []
for f1 in files:
    img = cv2.imread(f1)
    data.append(img)

x = img_to_array(img)
x = x.reshape((1,) + x.shape)

i = 0
path, dirs, files = next(os.walk("folder-name"))
file_count = len(files) #to find number of files in folder

for batch in datagen.flow (x, batch_size=1, save_to_dir =r'new-folder-name',save_prefix="a",save_format='jpg'):
    i+=1
    if i==file_count:
      break


