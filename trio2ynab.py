import sys
import os
import csv

path = os.path.splitext(sys.argv[1])
input = path[0] + path[1]
output = path[0] + "YNAB" + path[1]
transactions_trio = []
transactions_ynab = []

#Read Triodos csv
with open(input) as triodos_csv:
    csv_reader = csv.reader(triodos_csv)
    for line in csv_reader:
        transactions_trio.append(line)

#Convert
transactions_ynab.append(['Date', 'Payee', 'Memo', 'Outflow', 'Inflow'])
for transaction in transactions_trio:

    #Date
    date = transaction[0]

    #Payee
    if transaction[6] == 'BA':
        ba_splitted = transaction[7].split('\\')
        payee = ba_splitted[0] + ba_splitted[1]
    else:
        payee = transaction[4]

    #Memo
    if transaction[6] == 'BA':
        memo = 'Sven Rouschop'
    else:
        memo = transaction[7]

    #Inflow
    if transaction[3] == 'Credit':
        inflow = transaction[2]
    else:
        inflow = ''

    #Outflow
    if transaction[3] == 'Debet':
        outflow = transaction[2]
    else:
        outflow = ''

    transactions_ynab.append([date, payee, memo, inflow, outflow])

#Write bunq csv
with open(output, 'w') as ynab_csv:
    csv_writer = csv.writer(ynab_csv)
    for transaction in transactions_ynab:
        csv_writer.writerow(transaction)
