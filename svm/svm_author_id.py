#!/usr/bin/python3

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
print()

import math
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from collections import Counter

# Decrease size of training dataset
# features_train = features_train[: math.floor(len(features_train)/100)] 
# labels_train = labels_train[: math.floor(len(labels_train)/100)] 

clf = SVC(kernel='rbf', C=10000)

t_time = time()
clf.fit(features_train, labels_train)
print('Training time:', round(time() - t_time, 3), 's')

p_time = time()
pred = clf.predict(features_test)
print('Prediction time:', round(time() - p_time, 3), 's')

score = accuracy_score(labels_test, pred)

print('Accuracy: ', score)
print('Prediction 10: ', pred[10])
print('Prediction 26: ', pred[26])
print('Prediction 50: ', pred[50])
print('Counts (1 => Chris, 0 => Sarah): ', Counter(pred))
#########################################################


