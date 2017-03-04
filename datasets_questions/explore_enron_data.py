#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
<<<<<<< HEAD
import pprint
import decimal
pp = pprint.PrettyPrinter(indent=2)
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#Size of the Enron Dataset
print "The number of people in the enron dataset are:", len(enron_data)

#Features in the Enron Dataset
print "The number of features associated with each person:", len(enron_data["SKILLING JEFFREY K"])

#Finding POIs in the Enron Data
counter = 0
for k, v in enron_data.iteritems():
	if v["poi"] ==1:
		counter+=1
print "The number of POIs in the dataset:", counter

#How Many POIs Exist?
poi_names_file = open("../final_project/poi_names.txt", "r")
poi_names = [line.split('\n') for line in poi_names_file.readlines()][2:]
poi_names_2 = [filter(None,l) for l in poi_names]
print poi_names_2

#Query the Dataset 1
pp.pprint(enron_data["PRENTICE JAMES"])
print enron_data["PRENTICE JAMES"]['total_stock_value']
#Query the Dataset 2
print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

#Query the Dataset 3
print enron_data['SKILLING JEFFREY K']['exercised_stock_options']

#Follow the Money

print "Jeff Skilling:", enron_data['SKILLING JEFFREY K']['total_payments']
print "Ken Lay:", enron_data['LAY KENNETH L']['total_payments']
print "Andy Fastow:", enron_data['FASTOW ANDREW S']['total_payments']

#Dealing with Unfilled Features
salary_count = 0
email_count = 0
for k, v in enron_data.iteritems():
	if v['salary']!='NaN':
		salary_count+=1
	if v['email_address']!='NaN':
		email_count+=1
print "The number of quantifiable salaries in the dataset:", salary_count
print "The number of known email addresses in the dataset:", email_count

#Missing POIs 1 (optional)
total_count = 0
payment_count = 0
for k, v in enron_data.iteritems():
	if v['total_payments']=='NaN':
		payment_count+=1
	total_count+=1
percent_non_missing = float(payment_count)/total_count
print "The number of non-missing 'total payments' values in the dataset:", payment_count
print "Total number of observations:", total_count
print "%.2f" % percent_non_missing
	
#Missing POIs 2
poi_payment_count = 0
poi_count = 0
for k, v in enron_data.iteritems():
	if v['total_payments']=='NaN' and v["poi"] ==1:
		poi_payment_count+=1
	if v["poi"]==1:
		poi_count+=1
print "The number of POIs with missing 'total payments' in the dataset:", poi_payment_count
print "The number of POIs in the dataset:", poi_count

#Missing POIs 4
percent_non_missing2 = float(payment_count+10)/(total_count+10)
print percent_non_missing2
=======

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


>>>>>>> 8b79cb95d8573bc933059ac5deaaee1fd81452d5
