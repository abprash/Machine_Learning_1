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

# enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

def m1():
    """ getting the number of employees in the data corpus """
    enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
    print(str(len(enron_data)))

def m2():
    """getting the number of features per person """
    enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
    i = 0
    for employee in enron_data:
        print(employee)
        for feature in enron_data[employee]:
            print(feature+" --- "+str(enron_data[employee][feature]))

            i += 1
        break
    print(str(i))

def m3():
    """getting the number of POIs in the corpus """
    enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
    i = 0
    for employee in enron_data:
        # print(employee)
        if enron_data[employee]["poi"]:
            i += 1
    print(str(i))

def m4():
    enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
    for employee in enron_data:
        if "PRENTICE" in employee:
            print(enron_data[employee])

def m5():
    enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
    for employee in enron_data:
        if "COLWELL" in employee:
            print(enron_data[employee]["from_this_person_to_poi"])

def m6():
    enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
    for employee in enron_data:
        if "SKILLING" in employee:
            print(enron_data[employee])


if __name__ == "__main__":
    m6()
