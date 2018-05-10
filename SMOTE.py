from collections import Counter
from sklearn.datasets import make_classification
from imblearn.over_sampling import SMOTE


def SMOTEd(data,labels):
    """" Apply Synthetic Minority Over-sampling Technique (SMOTE) to data to deal with the imbalancedness of the data"""
    print('Original dataset shape {}'.format(Counter(labels)))
    sm = SMOTE()
    data_res, label_res = sm.fit_sample(data,labels)
    print('SMOTEd dataset shape {}'.format(Counter(label_res)))
    return data_res, label_res

