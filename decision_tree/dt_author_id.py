#!/usr/bin/python

"""
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import numpy

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###


#########################################################
def ex1():
    #create the classifier object
    classifier = DecisionTreeClassifier(min_samples_split=40)

    #fit with the training data and labels
    classifier.fit(features_train, labels_train)

    #do the prediction for test data
    predicted = classifier.predict(features_test)

    print str(accuracy_score(predicted, labels_test))

def ex2():
    #get the number of features from the training data
    # its the number of columns per row
    print str(numpy.shape(features_train)[1])

if __name__ == "__main__":
    ex1()
