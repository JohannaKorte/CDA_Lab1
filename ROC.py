from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt


def ROC_curve(cross_val_results):
    """ Given correct labels and predicted labels, give ROC curve"""

    keys = cross_val_results.keys()

    plt.figure()
    plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])
    plt.plot([0, 1], [0, 1], lw=2, linestyle='--')

    for key in keys:
        it = 0
        print key
        test_label = cross_val_results[key][0]
        y_pred = cross_val_results[key][1]

        # Compute TP, FP and area under the curve
        fpr, tpr, thresholds = roc_curve(test_label, y_pred)
        roc_auc = auc(fpr, tpr)

        # Compute optimal threshold
        # tpr - (1-fpr) is zero or near to zero is the optimal cut off point
        delta = 1000
        optimal = 0
        for i in range(len(thresholds)):
            distance = abs(tpr[i] - (1-fpr[i]))
            if distance < delta:
                optimal = i
                delta = distance
        print fpr[optimal]
        print tpr[optimal]

        threshold = thresholds[optimal]

        # Print TP, FP, FN, TN
        tp, fp, fn, tn = 0, 0, 0, 0
        for j in range(len(test_label)):
            if y_pred[j] > threshold and test_label[j] == 1:
                tp += 1
            elif y_pred[j] > threshold and test_label[j] == 0:
                fp += 1
            elif y_pred[j] <= threshold and test_label[j] == 1:
                fn += 1
            elif y_pred[j] <= threshold and test_label[j] == 0:
                tn += 1

        print "_______________"
        print "TP:      %i" % tp
        print "FP:      %i" % fp
        print "FN:      %i" % fn
        print "TN:      %i" % tn
        print "_______________"
        print "FPR:     %.2f" % fpr[optimal]
        print "TPR:     %.2f" % tpr[optimal]
        print "Threshold: %f" % threshold
        print "_______________"

        # Plot figure
        plt.plot(fpr, tpr,
                 lw=2, label='ROC %s (area = %0.2f)' % (key, roc_auc))
        it += 1

    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.legend(loc="lower right")
    plt.show()

    # # Compute TP, FP and area under the curve
    # fpr, tpr, roc_auc = {}, {}, {}
    # fpr, tpr, thresholds = roc_curve(test_label, y_pred)
    # roc_auc = auc(fpr, tpr)
    #
    # # Print optimal threshold
    # # tpr - (1-fpr) is zero or near to zero is the optimal cut off point
    # delta = 1000
    # optimal = 0
    # for i in range(len(thresholds)):
    #     distance = abs(tpr[i] - (1-fpr[i]))
    #     if distance < delta:
    #         optimal = i
    #         delta = distance
    # print fpr[optimal]
    # print tpr[optimal]
    #
    # threshold = thresholds[optimal]
    #
    # # Print TP, FP, FN, TN
    # tp, fp, fn, tn = 0, 0, 0, 0
    # for j in range(len(test_label)):
    #     if y_pred[j] > threshold and test_label[j] == 1:
    #         tp += 1
    #     elif y_pred[j] > threshold and test_label[j] == 0:
    #         fp += 1
    #     elif y_pred[j] <= threshold and test_label[j] == 1:
    #         fn += 1
    #     elif y_pred[j] <= threshold and test_label[j] == 0:
    #         tn += 1
    #
    # print "_______________"
    # print "TP:      %i" % tp
    # print "FP:      %i" % fp
    # print "FN:      %i" % fn
    # print "TN:      %i" % tn
    # print "_______________"
    # print "FPR:     %.2f" % fpr[optimal]
    # print "TPR:     %.2f" % tpr[optimal]
    # print "Threshold: %f" % threshold
    # print "_______________"

    # Plot figure
    # plt.figure()
    # plt.plot(fpr, tpr, color='darkorange',
    #          lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
    # plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    # plt.xlim([0.0, 1.0])
    # plt.ylim([0.0, 1.05])
    # plt.xlabel('False Positive Rate')
    # plt.ylabel('True Positive Rate')
    # plt.legend(loc="lower right")
    # plt.show()