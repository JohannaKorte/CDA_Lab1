#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Preprocess, apply SMOTE, and use crossvalidation to train a specific classifier on the supplied data
"""

import preprocess
import crossvalidation
import SMOTE
import ROC

__author__ = "Johanna Korte"
__email__ = "j.p.korte@student.tudelft.nl"

#  PARAMETERS
# ______________________________________________________________________________________________________________________

file = '/Users/johannakorte/Desktop/CDA_Lab1/data_for_student_case.csv'     # Input file
k = 10                                       # k-fold cross-validation parameter
classifier = 'neuralnetwork'                 # Choose classifier ('linear', 'decision tree', 'neuralnetwork', 'SVM')
SMOTEd = True                                # Apply SMOTE? (True, False)

#  MAIN
# ______________________________________________________________________________________________________________________

# Read and pre-process data
print "Preprocessing data..."
data, labels = preprocess.preprocess(file)

# Apply SMOTE if applicable and use k-fold cross-validation with the specified classifier
print "Applying %i-fold cross-validation, using %s classifier..." %(k, classifier)
test_label, predicted = crossvalidation.cross_val(data, labels, k, SMOTEd, classifier)

# ROC curve
print "Make ROC curve..."
ROC.ROC_curve(test_label, predicted)
print "Done."
