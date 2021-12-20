import pandas as pd

import os
print("PYTHONPATH:", os.environ.get('PYTHONPATH'))
print("PATH:", os.environ.get('PATH'))

# from data_loader import DataFolder
#
# train_dataset = DataFolder(root_directory= r'C:\Users\alexa\University\Master\DSP-A2\DSPA2\dataset\train_data', transform=train_transform)
# test_dataset = DataFolder(root_directory= r'C:\Users\alexa\University\Master\DSP-A2\DSPA2\dataset\test_data', transform=None)
#
# batch_size = 64
# train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
# test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=True)
# print(len(train_dataset))
# print(len(test_dataset))