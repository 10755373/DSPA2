from IPython.display import Image 
from PIL import Image
from torch.utils.data import Dataset
from torchvision import transforms
import albumentations as A 
from albumentations.pytorch  import ToTensorV2
from torch.utils.data import DataLoader, Dataset, WeightedRandomSampler
import torch
from torchvision.utils import make_grid
from matplotlib import pyplot as plt
import numpy as np
import os 
import re

class DataFolder(Dataset):
    def __init__(self, root_directory, transform=None):
        super(DataFolder,self).__init__() 
        self.data = []
        self.root_directory = root_directory
        self.transform = transform
        self.class_names= os.listdir(root_directory)
        # Loop through the folders and add labels to it signs:0 , notsigns: 1 
        for index_labels, name in enumerate(self.class_names):
            if name == 'cctvsign':
                files_data = os.listdir(os.path.join(root_directory,name))
                self.data += list(zip(files_data, [index_labels]*len(files_data)))
            else:
                files_data = os.listdir(os.path.join(root_directory,name))
                self.data += list(zip(files_data, [index_labels]*len(files_data)))
                
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, index):
        img_name , label = self.data[index]
        root_and_dir = os.path.join(self.root_directory,self.class_names[label])
        #Traffic sign images have 4 channels need to be converted to 3 with conver RGB
        image = np.array(Image.open(os.path.join(root_and_dir,img_name)).convert("RGB"))

        if self.transform is not None:
            augmentations_images= self.transform(image=image)
            image = augmentations_images['image']

        return image, label

train_transform = A.Compose(
    [
        A.Resize(35,35),
        A.HorizontalFlip(p=0.65),
        A.VerticalFlip(p=0.65),
        A.Rotate(limit=40,p=0.65),
        A.RGBShift(r_shift_limit=25, g_shift_limit=25,b_shift_limit=25,p=0.65),
        A.Normalize(
            mean=(0,0,0),
            std =(1,1,1),
            max_pixel_value=225,
        p=1),
        A.OneOf([
            A.Blur(blur_limit=3, p=0.65),
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
train_dataset = DataFolder(root_directory= r'C:\Users\Invitado\Documents\Python\DS_MASTER\DSP\dataset\train_data',transform=train_transform)
test_dataset = DataFolder(root_directory= r'C:\Users\Invitado\Documents\Python\DS_MASTER\DSP\dataset\test_data',transform=test_transform)
#Sampler to correct randomized batch in dataloader
#list of labels, and class number function 

def classes(dataset):
    class_cctv =0 
    class_not_cctv= 0
    labels_list = []
    for x, y in dataset:
        if y ==0:
            class_cctv  += 1
            labels_list.append(y)
        if y==1:
            class_not_cctv += 1
            labels_list.append(y)
    return class_cctv,class_not_cctv,labels_list

#sampler function
def sampler(class_1,class_2,labels_list):
    class_total_count = [class_1,class_2]
    weights_class = 1./torch.tensor(class_total_count, dtype=torch.float) 
    class_weights_all = weights_class [labels_list]
    balanced_sampler = WeightedRandomSampler(
        weights=class_weights_all,
        num_samples=len(class_weights_all),
        replacement=True
    )
    return balanced_sampler


train_data_sampler  = classes(train_dataset)
test_data_sampler  = classes(test_dataset)

sampler_train = sampler(train_data_sampler[0],train_data_sampler[1],train_data_sampler[2]) 
sampler_test = sampler(test_data_sampler[0],test_data_sampler[1],test_data_sampler[2])


batch_size = 64
train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size,sampler=sampler_train)
test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size,sampler = sampler_test)
print(len(train_dataset))
print(len(test_dataset))

# /Users/rinusvangrunsven/Documents/GitHub/DSPA2/dataset/train_data
