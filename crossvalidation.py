from sklearn.model_selection import KFold
import classifiers
import SMOTE


def cross_val_main(data, labels, k, smote, classifier):
    """ Main function to call cross_val over all specified classifiers"""
    cross_val_results = {}
    for i, c in enumerate(classifier):
        smoted = smote[i]
        print "Training %s %s..." % (c, smoted)
        cross_val_results[c+str(smoted)] = cross_val(data, labels, k, smoted, c)
    return cross_val_results


def cross_val(data, labels, k, smote, classifier):
    """ Performs k-fold cross validation using the specified classifier, returns number of true/false
    positives/negatives """
    kf = KFold(n_splits=k)
    tp, fp, fn, tn = 0, 0, 0, 0
    i = 0
    for train_index, test_index in kf.split(data):
            print i
            i += 1
            test_set, train_set, test_label, train_label = [], [], [], []
            # make train and test sets/labels
            for i in train_index:
                train_set.append(data[i])
                train_label.append(labels[i])
            for i in test_index:
                test_set.append(data[i])
                test_label.append(labels[i])

            # Apply SMOTEing when smote parameter is True
            if smote:
                train_set, train_label = SMOTE.SMOTEd(train_set, train_label)

            if classifier == 'linear':
                predicted = classifiers.lin_reg(train_set, test_set, train_label)
            elif classifier == 'logistic':
                predicted = classifiers.log_reg(train_set, test_set, train_label)
            elif classifier == 'decision tree':
                predicted = classifiers.decision_tree(train_set, test_set, train_label)
            elif classifier == 'neuralnetwork':
                predicted = classifiers.neuralnetwork(train_set, test_set, train_label)
            elif classifier == 'naive bayes':
                predicted = classifiers.naive_bayes(train_set, test_set, train_label)
            elif classifier == 'randomforest':
                predicted = classifiers.randomforest(train_set, test_set, train_label)
            elif classifier == 'knn':
                predicted = classifiers.knn(train_set, test_set, train_label)
            else:
                print 'Wrong name supplied: %s' % classifier

    return [test_label, predicted]
