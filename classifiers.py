import numpy as np
from sklearn import linear_model, tree
from sklearn.neural_network import MLPClassifier


def lin_reg(train_set, test_set, train_label):
    """ Performs linear regression on data"""
    regr = linear_model.LinearRegression()
    regr.fit(train_set, train_label)
    test_set = np.array(test_set, dtype=float)
    y_pred = regr.predict(test_set)
    return y_pred


def decision_tree(train_set, test_set, train_label):
    """ Trains a decision tree classier on data"""
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(train_set, train_label)
    y_pred = clf.predict(test_set)
    return y_pred


def neuralnetwork(train_set, test_set, train_label):
    """ Trains a neural network classifier on data"""
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes = (5, 2), random_state = 1)
    clf = clf.fit(train_set, train_label)
    y_pred = clf.predict(test_set)
    return y_pred

