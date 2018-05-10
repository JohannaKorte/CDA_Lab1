import preprocess
import classifiers
import crossvalidation

#  PARAMETERS
# ______________________________________________________________________________________________________________________

file = '/Users/johannakorte/Desktop/CDA_Lab1/data_for_student_case.csv'     # Input file
k = 2                                       # k-fold cross-validation parameter
classifier = 'linear'                       # Choose classifier ('linear', '', '')
SMOTEd = True                               # Apply SMOTE? (True, False)

#  MAIN
# ______________________________________________________________________________________________________________________

# Read and pre-process data
data, labels = preprocess.preprocess(file)

# Apply k-fold cross-validation with the specified classifier
tp, fp, fn, tn = crossvalidation.cross_val(data, labels, k, classifier)


#  PRINT RESULTS
# ______________________________________________________________________________________________________________________
print "TP:   ", tp
print "FP:   ", fp
print "FN:   ", fn
print "TN:   ", tn