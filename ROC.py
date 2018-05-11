from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt


def ROC_curve(test_label, y_pred):
    """ Given correct labels and predicted labels, give ROC curve"""

    # Compute TP, FP and area under the curve
    fpr, tpr, roc_auc = {}, {}, {}
    fpr, tpr, _ = roc_curve(test_label, y_pred)
    roc_auc = auc(fpr, tpr)

    # Plot figure
    plt.figure()
    plt.plot(fpr, tpr, color='darkorange',
             lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.legend(loc="lower right")
    plt.show()
