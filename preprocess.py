import csv
import numpy as np


def preprocess(file):
    """ Takes an input .csv file and preprocesses the data to floats. See report for more information """
    data = []
    labels = []

    with open(file, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        issuercountry_list, txvariantcode_list, currencycode_list, shoppercountrycode_list, \
        shopperinteraction_list, accountcode_list = [], [], [], [], [], []
        for row in reader:
            #Assign labels
            if row[9] == 'Chargeback' or row[9] == 'Settled':
                if row[9] == 'Chargeback':
                    labels.append(1)
                if row[9] == 'Settled':
                    labels.append(0)

                # Booking date
                # bookingdate = row[1]              # Leave out for now

                # Issuer country
                issuercountry = row[2]
                issuercountry_list.append(issuercountry)

                # TX variant code
                txvariantcode = row[3]
                txvariantcode_list.append(txvariantcode)

                # Bin
                bin = float(row[4])

                # Amount
                amount = float(row[5])/100

                # Currency Code
                currencycode = row[6]
                currencycode_list.append(currencycode)

                # Shopper country code
                shoppercountrycode = row[7]
                shoppercountrycode_list.append(shoppercountrycode)

                # Shopper interaction
                shopperinteraction = row[8]
                shopperinteraction_list.append(shopperinteraction)

                # Card Verification Code supplied?
                cvcsupplied = row[10]
                if cvcsupplied == 'True':
                    cvcsupplied = 1.0
                else:
                    cvcsupplied = 0.0

                # CVC match?
                # 0 = Unknown, 1=Match, 2=No Match, 3-6=Not checked
                cvcresponsecode = row[11]
                if int(cvcresponsecode) >= 3:
                    cvcresponsecode = 3
                cvcresponsecode = float(cvcresponsecode)

                # Creation date
                # creationdate = row[12]

                # Account code
                accountcode = row[13]
                accountcode_list.append(accountcode)

                # Mail id
                mail_id = row[14]
                mail_id = mail_id.replace('email', '')
                if mail_id == 'NA':
                    mail_id = 0.0
                else:
                    mail_id = float(mail_id)

                # Ip id
                ip_id = row[15]
                ip_id = ip_id.replace('ip', '')
                ip_id = float(ip_id)

                # Card id
                card_id = row[16]
                card_id = card_id.replace('card', '')
                card_id = float(card_id)

                instance = [issuercountry] + [txvariantcode] + [bin] + [amount] + [currencycode] + [shoppercountrycode] + \
                           [shopperinteraction] + [cvcsupplied] + [cvcresponsecode] + [accountcode] + [mail_id] + \
                           [ip_id] + [card_id]

                data.append(instance)

    # Make unique indices for every item in the list
    issuercountry_list = list(set(issuercountry_list))
    txvariantcode_list = list(set(txvariantcode_list))
    currencycode_list = list(set(currencycode_list))
    shoppercountrycode_list = list(set(shoppercountrycode_list))
    shopperinteraction_list = list(set(shopperinteraction_list))
    accountcode_list = list(set(accountcode_list))

    # Reassign item to the unique index in the list
    for i in range(len(data)):
        data[i][0] = float(issuercountry_list.index(data[i][0]))
        data[i][1] = float(txvariantcode_list.index(data[i][1]))
        data[i][4] = float(currencycode_list.index(data[i][4]))
        data[i][5] = float(shoppercountrycode_list.index(data[i][5]))
        data[i][6] = float(shopperinteraction_list.index(data[i][6]))
        data[i][9] = float(accountcode_list.index(data[i][9]))

    return data, labels
