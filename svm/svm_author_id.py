#!/usr/bin/python

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
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import numpy as np
from datetime import datetime





### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


""" """
# if we need a trimmed down training data - 1%
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]


#########################################################
### your code goes here ###

#########################################################
def start():
    #start time
    # start_time = time.time()
    start_time = datetime.now()
    C_values = [10, 100, 1000, 10000]
    #create a new classifier - with kernel as rbf/ linear
    # clf = SVC(kernel = "linear")
    clf = SVC(kernel = "rbf", C = 10)
    #fit the classifier
    clf.fit(features_train, labels_train)
    #predict the test data with it
    predicted = clf.predict(features_test)
    print predicted
    #elapsed time
    elapsed_time = datetime.now() - start_time
    print "Time taken = "+str(elapsed_time/60)+" mins."
    print "Accuracy = "+str(accuracy_score(labels_test,predicted))


def get_classifier(kernel_name, c_val):
    start_time = datetime.now()
    clf = SVC(kernel = kernel_name, C = c_val)
    #fit the classifier
    clf.fit(features_train, labels_train)
    #predict the test data with it
    predicted = clf.predict(features_test)
    # print predicted
    #elapsed time
    elapsed_time = datetime.now() - start_time
    print "Time taken = "+str(elapsed_time/60)
    print "C Value = "+str(c_val)+" Accuracy = "+str(accuracy_score(labels_test,predicted))
    return predicted

if __name__ == "__main__":
    C_values = [10, 100, 1000, 10000]
    #optimal C value is 10,000
    predicted = get_classifier("rbf", 10000)
    print "Element 10 - "+str(predicted[10])
    print "Element 26 - "+str(predicted[26])
    print "Element 50 - "+str(predicted[50])
    unique, counts = np.unique(np.array(predicted), return_counts=True)
    print dict(zip(unique, counts))
