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
def poiEmails():
    email_list = ["kenneth_lay@enron.net",
            "kenneth_lay@enron.com",
            "klay.enron@enron.com",
            "kenneth.lay@enron.com",
            "klay@enron.com",
            "layk@enron.com",
            "chairman.ken@enron.com",
            "jeffreyskilling@yahoo.com",
            "jeff_skilling@enron.com",
            "jskilling@enron.com",
            "effrey.skilling@enron.com",
            "skilling@enron.com",
            "jeffrey.k.skilling@enron.com",
            "jeff.skilling@enron.com",
            "kevin_a_howard.enronxgate.enron@enron.net",
            "kevin.howard@enron.com",
            "kevin.howard@enron.net",
            "kevin.howard@gcm.com",
            "michael.krautz@enron.com"
            "scott.yeager@enron.com",
            "syeager@fyi-net.com",
            "scott_yeager@enron.net",
            "syeager@flash.net",
            "joe'.'hirko@enron.com",
            "joe.hirko@enron.com",
            "rex.shelby@enron.com",
            "rex.shelby@enron.nt",
            "rex_shelby@enron.net",
            "jbrown@enron.com",
            "james.brown@enron.com",
            "rick.causey@enron.com",
            "richard.causey@enron.com",
            "rcausey@enron.com",
            "calger@enron.com",
            "chris.calger@enron.com",
            "christopher.calger@enron.com",
            "ccalger@enron.com",
            "tim_despain.enronxgate.enron@enron.net",
            "tim.despain@enron.com",
            "kevin_hannon@enron.com",
            "kevin'.'hannon@enron.com",
            "kevin_hannon@enron.net",
            "kevin.hannon@enron.com",
            "mkoenig@enron.com",
            "mark.koenig@enron.com",
            "m..forney@enron.com",
            "ken'.'rice@enron.com",
            "ken.rice@enron.com",
            "ken_rice@enron.com",
            "ken_rice@enron.net",
            "paula.rieker@enron.com",
            "prieker@enron.com",
            "andrew.fastow@enron.com",
            "lfastow@pdq.net",
            "andrew.s.fastow@enron.com",
            "lfastow@pop.pdq.net",
            "andy.fastow@enron.com",
            "david.w.delainey@enron.com",
            "delainey.dave@enron.com",
            "'delainey@enron.com",
            "david.delainey@enron.com",
            "'david.delainey'@enron.com",
            "dave.delainey@enron.com",
            "delainey'.'david@enron.com",
            "ben.glisan@enron.com",
            "bglisan@enron.com",
            "ben_f_glisan@enron.com",
            "ben'.'glisan@enron.com",
            "jeff.richter@enron.com",
            "jrichter@nwlink.com",
            "lawrencelawyer@aol.com",
            "lawyer'.'larry@enron.com",
            "larry_lawyer@enron.com",
            "llawyer@enron.com",
            "larry.lawyer@enron.com",
            "lawrence.lawyer@enron.com",
            "tbelden@enron.com",
            "tim.belden@enron.com",
            "tim_belden@pgn.com",
            "tbelden@ect.enron.com",
            "michael.kopper@enron.com",
            "dave.duncan@enron.com",
            "dave.duncan@cipco.org",
            "duncan.dave@enron.com",
            "ray.bowen@enron.com",
            "raymond.bowen@enron.com",
            "'bowen@enron.com",
            "wes.colwell@enron.com",
            "dan.boyle@enron.com",
            "cloehr@enron.com",
            "chris.loehr@enron.com"
        ]
    return email_list

import pickle


enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

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
"""
{'salary': 'NaN', 'to_messages': 'NaN', 'deferral_payments': 564348, 'total_payments': 564348, 'exercised_stock_options': 886231,
'bonus': 'NaN', 'restricted_stock': 208809, 'shared_receipt_with_poi': 'NaN', 'restricted_stock_deferred': 'NaN',
'total_stock_value': 1095040, 'expenses': 'NaN', 'loan_advances': 'NaN', 'from_messages': 'NaN', 'other': 'NaN',
'from_this_person_to_poi': 'NaN', 'poi': False, 'director_fees': 'NaN', 'deferred_income': 'NaN', 'long_term_incentive': 'NaN',
'email_address': 'james.prentice@enron.com', 'from_poi_to_this_person': 'NaN'}

"""
def m7():
    """find the num of ppl who have quantified salaries and known emails"""
    salary_num = 0
    known_emails = 0
    for employee in enron_data:
        if(enron_data[employee]["email_address"] != 'NaN'):
            known_emails += 1
        if enron_data[employee]["salary"] != "NaN":
            salary_num += 1
    print("Known emails - "+str(known_emails)+", salaried ppl - "+str(salary_num))

def m8():
    """find the percent of ppl who have NaN total payments """
    total = len(enron_data)
    print(total)
    payments_nan = 0.0
    for employee in  enron_data:
        if(enron_data[employee]["total_payments"] == "NaN"):
            payments_nan += 1
    print(payments_nan)
    print(str((payments_nan/total) * 100))

if __name__ == "__main__":
    m8()
