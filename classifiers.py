import numpy as np
from sklearn import linear_model, tree, svm
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier


def lin_reg(train_set, test_set, train_label):
    """ Performs linear regression on data"""
    regr = linear_model.LinearRegression()
    regr.fit(train_set, train_label)
    y_pred = regr.predict(test_set)
    return y_pred


def log_reg(train_set, test_set, train_label):
    """ Trains a logistic regression classifier on data"""
    regr = linear_model.LogisticRegression()
    regr.fit(train_set, train_label)
    y_pred = regr.predict(test_set)
    return y_pred


def decision_tree(train_set, test_set, train_label):
    """ Trains a decision tree classier on data"""
    clf = tree.DecisionTreeClassifier()
    clf.fit(train_set, train_label)
    y_pred = clf.predict(test_set)
    return y_pred


def neuralnetwork(train_set, test_set, train_label):
    """ Trains a neural network classifier on data"""
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state = 1)
    clf.fit(train_set, train_label)
    y_pred = clf.predict(test_set)
    return y_pred


def SVM(train_set, test_set, train_label):
    """ Trains a support vector machine (SVM) classifier on data"""
    clf = svm.SVC()
    clf.fit(train_set, train_label)
    y_pred = clf.predict(test_set)
    return y_pred


def naive_bayes(train_set, test_set, train_label):
    """ Trains a naive bayes classifier on data"""
    gnb = GaussianNB()
    gnb.fit(train_set, train_label)
    y_pred = gnb.predict(test_set)
    return y_pred


def randomforest(train_set, test_set, train_label):
    """ Trains forests of randomized trees classifier"""
    clf = RandomForestClassifier(n_estimators=10)
    clf.fit(train_set, train_label)
    y_pred = clf.predict(test_set)
    return y_pred
