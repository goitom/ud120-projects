#!/usr/bin/python

import sys
import pickle
import matplotlib.pyplot
import pprint
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data
### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
financial_features_list = ['poi', 
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
'director_fees']

email_features_list = ['poi', 'to_messages', 'email_address', 
'from_poi_to_this_person', 'from_messages', 'from_this_person_to_poi', 
'shared_receipt_with_poi']
### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

print "The dataset has", len(data_dict), "observations."
print "The dataset has", len(data_dict['CALGER CHRISTOPHER F']), "features."

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(stuff)
print(data_dict.keys())
### Task 2: Remove outliers
data_dict.pop('key', None)
data = featureFormat(data_dict, financial_features_list)

for point in data:
	salary = point[1]
	deferral_payments = point[2]
	total_payments = point[3]
	loan_advances = point[4]
	bonus = point[5]
	restricted_stock_deferred = point[6]
	deferred_income = point[7]
	total_stock_value = point[8]
	expenses = point[9]
	exercised_stock_options = point[10]
	other = point[11]
	long_term_incentive = point[12] 
	restricted_stock = point[13]
	director_fees = point[14]
	matplotlib.pyplot.scatter( salary, total_stock_value )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("total_stock_value")
matplotlib.pyplot.show()