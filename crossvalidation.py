from sklearn.model_selection import KFold
import classifiers


def cross_val(data, labels, k, classifier):
    """ ... """
    kf = KFold(n_splits=k)
    tp, fp, fn, tn = 0, 0, 0, 0
    for train_index, test_index in kf.split(data):
            test_set, train_set, test_label, train_label = [], [], [], []
            # make train and test sets/labels
            for i in train_index:
                train_set.append(data[i])
                train_label.append(labels[i])
            for i in test_index:
                test_set.append(data[i])
                test_label.append(labels[i])

            if classifier == 'linear':
                predicted = classifiers.lin_reg(train_set, test_set, train_label)
            elif classifier == 'decision tree':
                predicted = classifiers.decision_tree(train_set, test_set, train_label)
            elif classifier == 'neuralnetwork':
                predicted = classifiers.neuralnetwork(train_set, test_set, train_label)

            # Get TN,TP,FN,FP
            for i in range(len(predicted)):
                y_predicted = round(predicted[i])
                y_label = round(test_label[i])
                if y_predicted == 1 and y_label == 1:
                    tp += 1
                elif y_predicted == 1 and y_label == 0:
                    fp += 1
                elif y_predicted == 0 and y_label == 1:
                    fn += 1
                elif y_predicted == 0 and y_label == 0:
                    tn += 1

    tp /= k
    fp /= k
    fn /= k
    tn /= k
    return tp, fp, fn, tn
