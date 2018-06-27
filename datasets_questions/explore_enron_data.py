#!/usr/bin/python3

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
#%%
import pickle
import sys
sys.path.append("../final_project/")
from poi_email_addresses import poiEmails

enron_data = pickle.load(open("../final_project/final_project_dataset_unix.pkl", "rb"))

poi_count = {k:v for k,v in enron_data.items() if v['poi'] == 1}
print('POI Count: ', len(poi_count))

print('Email Count: ', len(poiEmails()))

print(f"James Prentice stock value: ${enron_data['PRENTICE JAMES']['total_stock_value']}")

print(f"Skilling profits: ${enron_data['SKILLING JEFFREY K']['total_payments']}")
print(f"Lay profits: ${enron_data['LAY KENNETH L']['total_payments']}")
print(f"Fastow profits: ${enron_data['FASTOW ANDREW S']['total_payments']}")

with_salary = {k:v for k,v in enron_data.items() if v['salary'] != 'NaN'}
print('Employees w/ quantified salary: ', len(with_salary))

with_email = {k:v for k,v in enron_data.items() if v['email_address'] != 'NaN'}
print('Employees w/ known email: ', len(with_email))

no_total = {k:v for k,v in enron_data.items() if v['total_payments'] == 'NaN'}
print(len(no_total))
no_total_percent = (len(no_total) / len(enron_data)) * 100
print(f'Percent with no total: {no_total_percent}%')

poi_no_total = {k:v for k,v in enron_data.items() if v['poi'] == 'true' and v['total_payments'] == 'NaN'}
print('POIs with no total payments: ', len(poi_no_total))

print(len(enron_data))