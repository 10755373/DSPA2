from IPython.display import Image 
from PIL import Image
from torch.utils.data import Dataset
from torchvision import transforms
import albumentations as A 
from albumentations.pytorch  import ToTensorV2
from torch.utils.data import DataLoader, Dataset
from torchvision.utils import make_grid
from matplotlib import pyplot as plt
import numpy as np
import os 
import re

class DataFolder(Dataset):
    def __init__(self, root_dir, transform=None):
        super(DataFolder,self).__init__() 
        self.data = []
        self.root_dir = root_dir
        self.transform = transform
        self.class_names= os.listdir(root_dir)
        # Loop through the folders and add labels to it signs:0 , notsigns: 1 
        for index, name in enumerate(self.class_names):
            if name == 'cctvsign':
                files = os.listdir(os.path.join(root_dir,name))
                self.data += list(zip(files, [index]*len(files)))
            else:
                files = os.listdir(os.path.join(root_dir,name))
                self.data += list(zip(files, [index]*len(files)))
                
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, index):
        img_file , label = self.data[index]
        root_and_dir = os.path.join(self.root_dir,self.class_names[label])
        image = np.array(Image.open(os.path.join(root_and_dir,img_file)).convert('RGB'))

        if self.transform is not None:
            augmentations= self.transform(image=image)
            image = augmentations['image']

        return image, label

train_transform = A.Compose(
    [
        A.Resize(35,35),
        A.HorizontalFlip(p=0.5),
        A.VerticalFlip(p=0.6),
        A.Rotate(limit=40,p=0.9),
        A.RGBShift(r_shift_limit=25, g_shift_limit=25,b_shift_limit=25,p=0.8),
        A.Normalize(
            mean=(0,0,0),
            std =(1,1,1),
            max_pixel_value=225,
        p=1),
        A.OneOf([
            A.Blur(blur_limit=3, p=0.5),
            A.ColorJitter(p=0.5)
        ],p=1.0),
        
        ToTensorV2(),
    ]
)
test_transform = A.Compose(
    [
        A.Resize(35,35),
        A.Normalize(
            mean=(0,0,0),
            std =(1,1,1),
            max_pixel_value=225,
        p=1),
        
        ToTensorV2(),
    ]
)

#Load the datasets 
train_dataset = DataFolder(root_dir= r'C:\Users\Invitado\Documents\Python\DS_MASTER\DSP\dataset\train_data',transform=train_transform)
test_dataset = DataFolder(root_dir= r'C:\Users\Invitado\Documents\Python\DS_MASTER\DSP\dataset\validation_data',transform=None)

batch_size = 64
train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=True)
