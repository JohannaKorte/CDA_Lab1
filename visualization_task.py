import pickle
import numpy as np
import matplotlib.pyplot as plt
import preprocess

file = '/Users/johannakorte/Desktop/CDA_Lab1/data_for_student_case.csv'

data, labels = preprocess.preprocess(file)

settled_amounts = [x[3] for i, x in enumerate(data) if labels[i] == 0]
chargeback_amounts = [x[3] for i, x in enumerate(data) if labels[i] == 1]

# Weigths to enable percentage y-axis
settled_length = len(settled_amounts)
chargeback_length = len(chargeback_amounts)
weights_settled = np.ones_like(settled_amounts)/float(len(settled_amounts))
weights_chargeback = np.ones_like(chargeback_amounts)/float(len(chargeback_amounts))


plt.figure()
f, (ax1, ax2) = plt.subplots(2,1,sharex=True, sharey=True, tight_layout=True)
ax1.hist(settled_amounts, weights=weights_settled, bins=100, color='#00A6D6')
ax2.hist(chargeback_amounts, weights=weights_chargeback, bins=100, color='#008891')
ax1.set_title('Settled')
ax2.set_title('Chargeback')
ax2.set_xlabel('Amount')
ax1.set_ylabel('Fraction of transactions')
ax2.set_ylabel('Fraction of transactions')
plt.axis([0, 8000, 0, 0.9])
plt.show()



