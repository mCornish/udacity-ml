#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset_unix.pkl", "rb") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list, sort_keys = '../tools/python2_lesson14_keys_unix.pkl')
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=.3, random_state=42)
clf = DecisionTreeClassifier().fit(features_train, labels_train)
pred = clf.predict(features_test)
acc = accuracy_score(labels_test, pred)
prec = precision_score(labels_test, pred)
rec = recall_score(labels_test, pred)

poi_count = 0
for result in pred:
    if (result == 1):
        poi_count += 1

true_positives = 0
for index, label in enumerate(labels_test):
    if (labels_test[index] == 1 and labels_test[index] == pred[index]):
        true_positives += 1

print('Employee Count: ', len(features_test))
print('POI Count: ', poi_count)
print('Accuracy: ', acc)
print('Precision: ', prec)
print('Recall: ', rec)
print('True Positives: ', true_positives)
