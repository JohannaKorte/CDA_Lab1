import pickle
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt

f = open('dataframe.pckl', 'rb')
data = pickle.load(f)
f.close()

x = 'simple_journal'

Xuniques, X = np.unique(data[x], return_inverse=True)
print Xuniques

# settled_amount_values = [x for i,x in enumerate(data['amount']) if data['simple_journal'][i] == 'Settled']
# chargeback_amount_values = [x for i,x in enumerate(data['amount']) if data['simple_journal'][i] == 'Chargeback']
# refused_amount_values = [x for i,x in enumerate(data['amount']) if data['simple_journal'][i] == 'Refused']
#
# settled_x = [X[i] for i,x in enumerate(data['amount']) if data['simple_journal'][i] == 'Settled']
# chargeback_x = [X[i] for i,x in enumerate(data['amount']) if data['simple_journal'][i] == 'Chargeback']
# refused_x = [X[i] for i,x in enumerate(data['amount']) if data['simple_journal'][i] == 'Refused']

fig = plt.figure()
ax = fig.add_subplot(111)
# ax.scatter(settled_x ,settled_amount_values, c='b', marker='s')
# ax.scatter(chargeback_x,chargeback_amount_values, c='r', marker='s')
# ax.scatter(refused_x,refused_amount_values,c='g',marker='s')
ax.scatter(X,data['amount'])
ax.set(xticks=range(len(Xuniques)), xticklabels=Xuniques)
plt.legend(loc='upper left')
plt.show()
