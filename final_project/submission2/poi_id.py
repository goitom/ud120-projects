#!/usr/bin/python

import sys
import pickle
import pprint
import matplotlib.pyplot
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data
### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
raw_features_list = ['poi',
'salary', 
'deferral_payments', 
'total_payments', 
'loan_advances', 
'bonus', 
'restricted_stock_deferred', 
'deferred_income', 
'total_stock_value', 
'expenses', 
'exercised_stock_options', 
'other', 
'long_term_incentive', 
'restricted_stock', 
'director_fees',
'to_messages', 
'from_poi_to_this_person', 
'from_messages', 
'from_this_person_to_poi', 
'shared_receipt_with_poi']

features_list = ['poi',
'salary', 
'bonus', 
'total_stock_value',
'pct_email_shared_reciept',
'pct_email_from_poi',
'pct_email_to_poi'
]


### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

# Determine the Number of observations and features in the dataset
print "The dataset has", len(data_dict), "observations."
print "The dataset has", len(data_dict['CALGER CHRISTOPHER F']), "features."

poi_counter = 0
non_poi_counter = 0
for k, v in data_dict.iteritems():
	if v['poi'] == True:
		poi_counter=poi_counter+1
	elif v['poi'] == False:
		non_poi_counter=non_poi_counter+1

print "Number of POIs:", str(poi_counter)
print "Number of Non POIs", str(non_poi_counter)
### Task 2: Remove outliers

## Identify outliers in financial features
financial_features_list = ['salary', 'total_stock_value']

### Task 2: Remove outliers
outlier_check = featureFormat(data_dict, financial_features_list)

for point in outlier_check:
	salary = point[0]
	total_stock_value = point[1]
	matplotlib.pyplot.scatter( salary, total_stock_value )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("total_stock_value")
matplotlib.pyplot.show()
# get list of keys to identify and remove outlier
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data_dict.keys())

# Remove outlier and confirm its removal with a second plot
data_dict.pop('TOTAL', None)
outlier_check = featureFormat(data_dict, financial_features_list)
pp.pprint(data_dict.keys())

for point in outlier_check:
	salary = point[0]
	total_stock_value = point[1]
	matplotlib.pyplot.scatter( salary, total_stock_value )

# matplotlib.pyplot.xlabel("salary")
# matplotlib.pyplot.ylabel("total_stock_value")
# matplotlib.pyplot.show()

## Remove missing values from dataset
temp_dict = {k: v for k, v in data_dict.iteritems() if \
(v['total_stock_value'] != 'NaN' or \
v['salary'] != 'NaN') and \
v['to_messages'] != 'NaN' and \
v['from_messages'] != 'NaN' \
}

### Task 3: Create new feature(s)
for k in temp_dict:
	temp_dict[k]['pct_email_to_poi'] = \
	float(temp_dict[k]['from_this_person_to_poi'])/float(temp_dict[k]['from_messages'])
	temp_dict[k]['pct_email_from_poi'] = \
	float(temp_dict[k]['from_poi_to_this_person'])/float(temp_dict[k]['to_messages'])
	temp_dict[k]['pct_email_shared_reciept'] = \
	float(temp_dict[k]['shared_receipt_with_poi'])/float(temp_dict[k]['to_messages'])

### Store to my_dataset for easy export below.
my_dataset = temp_dict

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html
from sklearn import preprocessing
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.feature_selection import SelectKBest, chi2, f_classif

scaler = preprocessing.MinMaxScaler()
features = scaler.fit_transform(features)

# Uncomment below to use SelectKBest
# skb = SelectKBest()

# Uncomment below to use Naive Bayes Classifier
# nb = GaussianNB()

svc = SVC()
param_grid = [
  {'SVC__C': [1, 10, 100, 1000, 10000], 'SVC__kernel': ['linear']},
  {'SVC__C': [1, 10, 100, 1000, 10000], 'SVC__gamma': [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0], 'SVC__kernel': ['rbf']}
 ]
# Implement Pipeline
gs =  Pipeline(steps=[('scaling',scaler), ("SVC", svc)])

# If using SelectKBest, then uncomment to list the selected features
# features_selected=[features_list[i+1] for i in skb.get_support(indices=True)]
# print 'Features selected by SelectKBest:'
# print features_selected

### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html
from sklearn.grid_search import GridSearchCV
from time import time
pp = pprint.PrettyPrinter(indent=4)

svcclf = GridSearchCV(gs, param_grid, scoring='f1', cv=10)
svcclf.fit(features, labels)
clf = svcclf.best_estimator_
print("Best parameters set found on development set:")
print()
print(svcclf.best_params_)
print()
print("Grid scores on development set:")
print()
for params, mean_score, scores in svcclf.grid_scores_:
    print("%0.3f (+/-%0.03f) for %r"
          % (mean_score, scores.std() * 2, params))
print()

from tester import test_classifier
test_classifier(clf, my_dataset, features_list, folds = 1000)

### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)
