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

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn import tree

features_train, features_test, labels_train, labels_test = train_test_split(
	features, labels, test_size=0.30, random_state=42)



### it's all yours from here forward! 
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

#print the total number of predicted POI in test data set
print sum(pred)

#print the number of people in the test data set
print len(pred)

#print the labels and the predicted values and compare
print "Actual POI indicators:", labels_test
print "Predicted POI indicators:", pred

acc = accuracy_score(pred, labels_test)
print "Accuracy is: ", acc

prec=precision_score(pred, labels_test)
print "Precision is: ", prec

recall=recall_score(pred, labels_test)
print "Recall is: ", recall

