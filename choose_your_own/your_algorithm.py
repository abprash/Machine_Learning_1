#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
import numpy

#import required modules
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

"""
1. We have the option to try out 3 different ML algorithms - k-nn, adaboost and random forest
2. We will try all 3, and compare the accuracy with respect to each other
3. Lets code!
"""


features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the
### visualization code (prettyPicture) to show you the decision boundary
def knn():
    classifier = KNeighborsClassifier()
    classifier.fit(features_train, labels_train)
    predicted = classifier.predict(features_test)
    print "K Nearest Neighbors = " + str(accuracy_score(labels_test, predicted))
    return classifier

def random_forest():
    classifier = RandomForestClassifier()
    classifier.fit(features_train, labels_train)
    predicted = classifier.predict(features_test)
    print "Random Forest Accuracy = " + str(accuracy_score(labels_test, predicted))
    return classifier

def adaboost():
    classifier = AdaBoostClassifier()
    classifier.fit(features_train, labels_train)
    predicted = classifier.predict(features_test)
    print "AdaBoost Accuracy = " + str(accuracy_score(labels_test, predicted))
    return classifier


if __name__ == "__main__":
    try:
        # clf = knn()
        # clf = adaboost()
        clf = random_forest()
        prettyPicture(clf, features_test, labels_test)
    except NameError:
        pass
