import numpy as np
from sklearn import linear_model


def lin_reg(train_set, test_set, train_label):
    """ Performs linear regression on data"""
    regr = linear_model.LinearRegression()
    regr.fit(train_set, train_label)
    test_set = np.array(test_set, dtype=float)
    y_pred = regr.predict(test_set)
    return y_pred