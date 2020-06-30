import sys
import os
import csv

path = os.path.splitext(sys.argv[1])
input = path[0] + path[1]
output = path[0] + "2YNAB" + path[1]
transactions_input = []
transactions_output = []
converter = None

#Converter clases take a list of transations with comma-seperated items and returns the same format
class N26Converter():
    def convert(self, input):
        output = []
        output.append(['Date', 'Payee', 'Memo', 'Outflow', 'Inflow'])
        input = input[1:]
        for transaction in transactions_input:
            date = transaction[0]
            payee = transaction[1]
            memo = transaction[4]
            outflow = ''
            inflow = transaction[6]
            output.append([date, payee, memo, outflow, inflow])
        return output

class TrioConverter():
    def convert(self, input):
        output = []
        output.append(['Date', 'Payee', 'Memo', 'Outflow', 'Inflow'])
        for transaction in transactions_input:
            date = transaction[0]
            if transaction[6] == 'BA':
                ba_split = transaction[7].split('\\')
                payee = ba_split[0] + ba_split[1]
                memo = ba_split[2]
            elif transaction[6] == 'KN':
                payee = 'Triodos Bank N.V.'
                memo = transaction[7]
            elif transaction[6] == 'GA':
                payee = 'GA'
                memo = transaction[7]
            else:
                payee = transaction[4]
                memo = transaction[7]
            if transaction[3] == 'Credit':
                inflow = transaction[2]
                outflow = ''
            if transaction[3] == 'Debet':
                inflow = ''
                outflow = transaction[2]
            output.append([date, payee, memo, outflow, inflow])
        return output

#Read csv
with open(input) as input_csv:

    csv_reader = csv.reader(input_csv)
    for line in csv_reader:
        transactions_input.append(line)

#Check bank type
if transactions_input[0] == ['Date', 'Payee', 'Account number', 'Transaction type', 'Payment reference', 'Category', 'Amount (EUR)', 'Amount (Foreign Currency)', 'Type Foreign Currency', 'Exchange Rate']:
    converter = N26Converter()
else:
    converter = TrioConverter()

#Convert
transactions_output = converter.convert(transactions_input)

#Write YNAB csv
with open(output, 'w') as output_csv:
    csv_writer = csv.writer(output_csv)
    for transaction in transactions_output:
        csv_writer.writerow(transaction)
