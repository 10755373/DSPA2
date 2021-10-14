# # PATH_TO_IMAGES = r'C:Users---practice/'
# PATH_TO_IMAGES = 'Users/rinusvangrunsven/Documents/GitHub/DSPA2/practice/test/'


# # Specify whatever augmentation methods you want to use here
# train_datagen = ImageDataGenerator(
#         rotation_range=30, 
#         width_shift_range=0.3,
#         height_shift_range=0.3, 
#         shear_range=0.2, 
#         zoom_range=0.2,
#         horizontal_flip=True, 
#         vertical_flip=True,
#         fill_mode='nearest')

# train_generator = train_datagen.flow_from_directory(
#         PATH_TO_IMAGES,
#         target_size=(150, 150),
#         batch_size=32,
#         save_to_dir=/tmp/img-data-gen-outputs
#         class_mode='binary')

# # Use the generator by calling .next()

# train_generator.next()

# -------------------------------------

# from keras.preprocessing.image import ImageDataGenerator
# from skimage import io
# datagen = ImageDataGenerator(        
#         rotation_range = 40,
#         shear_range = 0.2,
#         zoom_range = 0.2,
#         horizontal_flip = True,
#         brightness_range = (0.5, 1.5))
# import numpy as np
# import os
# from PIL import Image
# image_directory = r'C:Users---sign/'
# SIZE = 224
# dataset = []
# my_images = os.listdir(image_directory)
# for i, image_name in enumerate(my_images):    
#     if (image_name.split('.')[1] == 'jpg'):        
#         image = io.imread(image_directory + image_name)        
#         image = Image.fromarray(image, 'RGB')        
#         image = image.resize((SIZE,SIZE)) 
#         dataset.append(np.array(image))
# x = np.array(dataset)
# i = 0
# for batch in datagen.flow(x, batch_size=16,
#                           save_to_dir= r'C:Users---Augmented-images',
#                           save_prefix='dr',
#                           save_format='jpg'):    
#     i += 1    
#     if i > 50:        
#         break

# ----------------------------------------

# import sys
# import cv2
# import albumentations as A
# import numpy as np
# from utils import plot_examples
# from PIL import Image

# image = Image.open("/Users/rinusvangrunsven/Documents/GitHub/DSPA2/practice/signs- 12.jpeg")

# transform = A.Compose(
#     [
#         A.Resize(width=1920, height=1080),
#         A.RandomCrop(width=1280, height=720),
#         A.Rotate(limit=40, p=0.9, border_mode=cv2.BORDER_CONSTANT),
#         A.HorizontalFlip(p=0.5),
#         A.VerticalFlip(p=0.1),
#         A.RGBShift(r_shift_limit=25, g_shift_limit=25, b_shift_limit=25, p=0.9),
#         A.OneOf([
#             A.Blur(blur_limit=3, p=0.5),
#             A.ColorJitter(p=0.5),
#         ], p=1.0),
#     ]
# )

# images_list = [image]
# image = np.array(image)
# for i in range(15):
#     augmentations = transform(image=image)
#     augmented_img = augmentations["image"]
#     images_list.append(augmented_img)
# plot_examples(images_list)

# import sys
# print(sys.path)

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
    
    
    

