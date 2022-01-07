import data_loader
from data_loader import DataFolder
from __future__ import print_function, division

import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
import numpy as np
import torchvision
from torchvision import datasets, models, transforms
import matplotlib.pyplot as plt
import time
import os
import copy
import pandas as pd
from torch.utils.data import DataLoader
from sklearn.model_selection import KFold

def k_fold_train(model,data,optimizer,criterion,scheduler,k_folds=5, num_epochs=25, batch_size=64):  
    # Set fixed random number seed
    torch.manual_seed(42)

    kfold = KFold(n_splits=k_folds, shuffle=True)
    best_result = 0.0
    for fold, (train_ids, test_ids) in enumerate(kfold.split(data)):
        print('---- Fold {}/{} ----'.format(fold+1, k_folds))
    
        train_subsampler = torch.utils.data.SubsetRandomSampler(train_ids)
        test_subsampler = torch.utils.data.SubsetRandomSampler(test_ids)
    
        train_loader = DataLoader(dataset=data, batch_size=batch_size,sampler= train_subsampler)
        test_loader = DataLoader(dataset=data, batch_size=batch_size,sampler = test_subsampler)
    
        dataloaders = {'train': train_loader, 'test': test_loader}
        dataset_sizes = {'train': len(train_subsampler), 'test': len(test_subsampler)}
    
        since = time.time()

        best_model_wts = copy.deepcopy(model.state_dict())
        best_acc = 0.0

        for epoch in range(num_epochs):
            print('Epoch {}/{}'.format(epoch+1, num_epochs))
            print('-' * 10)

            # Each epoch has a training and validation phase
            for phase in ['train', 'test']:
                if phase == 'train':
                    model.train()  # Set model to training mode
                else:
                    model.eval()   # Set model to evaluate mode

                running_loss = 0.0
                running_corrects = 0

                # Iterate over data.
                for inputs, labels in dataloaders[phase]:
                    inputs = inputs.to(device)
                    labels = labels.to(device)

                # zero the parameter gradients
                    optimizer.zero_grad()

                    # forward
                    # track history if only in train
                    with torch.set_grad_enabled(phase == 'train'):
                        outputs = model(inputs)
                        _, preds = torch.max(outputs, 1)
                        loss = criterion(outputs, labels)

                        # backward + optimize only if in training phase
                        if phase == 'train':
                            loss.backward()
                            optimizer.step()

                    # statistics
                    running_loss += loss.item() * inputs.size(0)
                    running_corrects += torch.sum(preds == labels.data)
                if phase == 'train':
                    scheduler.step()

                epoch_loss = running_loss / dataset_sizes[phase]
                epoch_acc = running_corrects.double() / dataset_sizes[phase]

                print('{} Loss: {:.4f} Acc: {:.4f}'.format(
                    phase, epoch_loss, epoch_acc))

                # deep copy the model
                if phase == 'test' and epoch_acc > best_acc:
                    best_acc = epoch_acc
                    best_model_wts = copy.deepcopy(model.state_dict())

            print()

        time_elapsed = time.time() - since
        print('Training complete in {:.0f}m {:.0f}s'.format(
            time_elapsed // 60, time_elapsed % 60))
        print('Best val Acc: {:4f}'.format(best_acc))

        # load best model weights
        model.load_state_dict(best_model_wts)

        if best_acc > best_result:
            best_result=best_acc
            best_model=model
    print('Best val Acc after k-folds: {:4f}'.format(best_result))        
    model_fit=best_model
    return model_fit




plt.ion()   # interactive mode

k_folds = 5
num_epochs = 25
batch_size = 64

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

model = models.resnet18(pretrained=False)
num_ftrs = model.fc.in_features
# Here the size of each output sample is set to 2.
# Alternatively, it can be generalized to nn.Linear(num_ftrs, len(class_names)).
model.fc = nn.Linear(num_ftrs, 2)

model = model.to(device)

criterion = nn.CrossEntropyLoss()

# Observe that all parameters are being optimized
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

# Decay LR by a factor of 0.1 every 7 epochs
scheduler = lr_scheduler.StepLR(optimizer, step_size=5, gamma=0.1)
data = data_loader.train_dataset
model_fit = k_fold_train(model,data,optimizer,criterion,scheduler,k_folds,num_epochs,batch_size)