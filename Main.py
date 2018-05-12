#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Preprocess, apply SMOTE, and use crossvalidation to train a specific classifier on the supplied data
"""

import preprocess
import crossvalidation
import ROC

__author__ = "Johanna Korte"
__email__ = "j.p.korte@student.tudelft.nl"

#  PARAMETERS
# ______________________________________________________________________________________________________________________
# Input file
file = '/Users/johannakorte/Desktop/CDA_Lab1/data_for_student_case.csv'

# k-fold cross-validation parameter
k = 10

# Choose classifier ('linear', 'decision tree', 'neuralnetwork', 'SVM', 'naive bayes', 'randomforest', 'logistic')
classifier = ['decision tree', 'decision tree']

# Apply SMOTE? (True, False) per classifier
SMOTEd = [True, False]

#  MAIN
# ______________________________________________________________________________________________________________________

# Read and pre-process data
print "Preprocessing data..."
data, labels = preprocess.preprocess(file)

# Apply SMOTE if applicable and use k-fold cross-validation with the specified classifier
print "Applying %i-fold cross-validation, using %s classifier(s)..." %(k, tuple(classifier))
cross_val_results = crossvalidation.cross_val_main(data, labels, k, SMOTEd, classifier)

# Print ROC curve
ROC.ROC_curve(cross_val_results)

print "Done."
