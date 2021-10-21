# https://www.analyticsvidhya.com/blog/2021/06/offline-data-augmentation-for-multiple-images/
# this one looks really promissing, but I'm having the same problem as with testrinus2.py

import keras
from keras.preprocessing.image import ImageDataGenerator
from skimage import io
datagen = ImageDataGenerator(        
        rotation_range = 40,
        shear_range = 0.2,
        zoom_range = 0.2,
        horizontal_flip = True,
        brightness_range = (0.5, 1.5))
import numpy as np
import os
from PIL import Image
# image_directory = r'C:Users---train/'
image_directory = r'/Users/rinusvangrunsven/Documents/GitHub/DSPA2/practice/test/'

SIZE = 224
dataset = []
my_images = os.listdir(image_directory)
for i, image_name in enumerate(my_images):    
    if (image_name.split('.')[1] == 'jpg'):        
        image = io.imread(image_directory + image_name)        
        image = Image.fromarray(image, 'RGB')        
        image = image.resize((SIZE,SIZE)) 
        dataset.append(np.array(image))
x = np.array(dataset)
i = 0
for batch in datagen.flow(x, batch_size=6,
                        #   save_to_dir= r'C:Users---Augmented-images',
                          save_to_dir= r'/Users/rinusvangrunsven/Documents/GitHub/DSPA2/practice/augtest/',
                          save_prefix='dr',
                          save_format='jpg'):    
    i += 1    
    if i > 50:        
        break