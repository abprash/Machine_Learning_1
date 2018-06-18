#!/usr/bin/python

"""
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project.

    Use a Naive Bayes Classifier to identify emails by their authors

    authors and labels:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from datetime import datetime

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###


#########################################################
# we need to find out the elapsed time as well
start = datetime.now()

# create a Classifier
clf = GaussianNB()

# fit (ie train) the model
clf.fit(features_train, labels_train)
print "Model Trained !"

# predict using the trained model now
predicted = clf.predict(features_test)
print "Predicted !"

end = datetime.now()
print "Elapsed time = "+str(end-start)
print "Accuracy = "+str(accuracy_score(predicted, labels_test))
