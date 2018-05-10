import preprocess
import crossvalidation
import SMOTE

#  PARAMETERS
# ______________________________________________________________________________________________________________________

file = '/Users/johannakorte/Desktop/CDA_Lab1/data_for_student_case.csv'     # Input file
k = 10                                       # k-fold cross-validation parameter
classifier = 'decision tree'                 # Choose classifier ('linear', 'decision tree', 'neuralnetwork', 'SVM')
SMOTEd = True                                # Apply SMOTE? (True, False)

#  MAIN
# ______________________________________________________________________________________________________________________

# Read and pre-process data
print "Preprocessing data..."
data, labels = preprocess.preprocess(file)

# Apply oversampling if SMOTE is true in PARAMETERS
if SMOTEd:
    print "SMOTEing data..."
    data, labels = SMOTE.SMOTEd(data, labels)

# Apply k-fold cross-validation with the specified classifier
print "Applying %i-fold cross-validation, using %s..." %(k, classifier)
tp, fp, fn, tn = crossvalidation.cross_val(data, labels, k, classifier)


#  PRINT RESULTS
# ______________________________________________________________________________________________________________________
print "Done."
print "________________________"
print "Average TP, FP, FN, TN:"
print "TP:   ", tp
print "FP:   ", fp
print "FN:   ", fn
print "TN:   ", tn
