''' This file contains the random baseline prediction script that runs on the test set. '''

import albumentations as A
import numpy as np
import pandas as pd
from data_loader import DataFolder, classes, sampler
from torch.utils.data import DataLoader
from albumentations.pytorch import ToTensorV2
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score


def stats(data, columns, class_number):
    """ Returns the accuracy, precision, recall and f1-score for a dialogue act given a label and a prediction column in
        a DataFrame.

        Args:
            data            = a DataFrame consisting of columns containing predictions and labels
            column_names    = the columns in the DataFrame over which the precision and recall must be calculated
            class_number    = the class number for which the prediction, recall and must be calculated.
   """

    # True positive:    label == DA && prediction == DA
    # False positive:   label != DA && prediction == DA
    # False negative:   label == DA && prediction != DA
    # True negative:    label != DA && prediction != DA

    data_columns = data[columns]
    labels = columns[0]
    predictions = columns[1]

    # Computes the accuracy, the percentage of rows where both columns have an equal value.
    n_equal_columns = len(data[(data[labels] == data[predictions])])
    accuracy = n_equal_columns / len(data)

    # Computes the precision = true positives / (true positives + false positives).
    # All the DataFrame rows with the dialogue act in the prediction column (true positives + false positives)
    predictions_of_da = data_columns[data_columns[predictions] == class_number]

    # The true positives are the ones of which the label and the prediction are both the dialogue act.
    true_positives = len(predictions_of_da[predictions_of_da[labels] == class_number])

    # The number of the predictions of the dialogue act is the true positives and false positives combined.
    true_positives_and_false_positives = len(predictions_of_da)

    # Computes the recall.
    # All the DataFrame rows with the dialogue act in the label column (true positives + false negatives)
    true_positives_and_false_negatives = len(data_columns[data_columns[labels] == class_number])

    # If the number of labels as the dialogue act is 0, the recall is set to NaN.
    recall = np.nan
    if true_positives_and_false_negatives != 0:
        recall = true_positives / true_positives_and_false_negatives

    # If the number of predictions as the dialogue act is 0, the precision is set to NaN.
    precision = np.nan
    if true_positives_and_false_positives != 0:
        precision = true_positives / true_positives_and_false_positives
    elif recall == 0:
        precision = 0

    # If either the precision or the recall is NaN, the f1-score is set to NaN as well.
    f1 = np.nan
    if recall == 0:
        f1 = 0
    elif precision != np.nan and recall != np.nan:
        f1 = 2 * (precision * recall) / (precision + recall)

    return accuracy, precision, recall, f1

# Loads the datasets
test_transform = A.Compose([A.Resize(35, 35), A.Normalize(mean=(0, 0, 0), std=(1, 1, 1), max_pixel_value=225, p=1), ToTensorV2(), ])
test_dataset = DataFolder(root_directory=r'C:\Users\alexa\University\Master\DSP-A2\DSPA2\dataset\test_data', transform=test_transform)

# distributes classes evenly
test_data_sampler = classes(test_dataset)
sampler_test = sampler(test_data_sampler[0], test_data_sampler[1], test_data_sampler[2])

batch_size = 1
test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size, sampler=sampler_test)

# The CCTV sign class is labeled 0 and the other class is labeled 1
class_names = {'0': 'cctv', '1': 'other'}

# Creates a DataFrame with the random uniform prediction results
df = pd.DataFrame(columns=['labels', 'predictions'])
for _, label in test_loader:
    label = label.numpy()[0]
    prediction = np.random.randint(2, size=1)[0]
    df_entry = {'labels':label, 'predictions':prediction}
    df = df.append(df_entry, ignore_index=True)

# Stores the random predictions to a csv
df.to_csv('random_baseline_predictions.csv')

# Computes the test statistics of the predictions
for c in np.array([0, 1]):
    accuracy, precision, recall, f1 = stats(df, ['labels', 'predictions'], c)
    print(class_names.get(str(c)) + ' simple accuracy is: ' + str(round(accuracy, 4)))
    print(class_names.get(str(c)) + ' precision is: ' + str(round(precision, 4)))
    print(class_names.get(str(c)) + ' recall is: ' + str(round(recall, 4)))
    print(class_names.get(str(c)) + ' f1 is: ' + str(round(f1, 4)))

