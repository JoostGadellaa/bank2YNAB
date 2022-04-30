import sys
import os
import csv
import re

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
        for transaction in transactions_input:
            date = transaction[0]
            payee = transaction[1]
            memo = clean(transaction[4])
            outflow = ''
            inflow = transaction[6]
            output.append([date, payee, memo, outflow, inflow])
        return output

class RaboConverter():
    def convert(self, input):
        output = []
        output.append(['Date', 'Payee', 'Memo', 'Outflow', 'Inflow'])
        for transaction in transactions_input:
            date = transaction[4]
            payee = transaction[9]
            memo = clean(transaction[19])
            outflow = ''
            inflow = transaction[6]
            output.append([date, payee, memo, outflow, inflow])
        return output

class ASNConverter():
    def convert(self, input):
        output = []
        output.append(['Date', 'Payee', 'Memo', 'Outflow', 'Inflow'])
        for transaction in transactions_input:
            date = transaction[0]
            outflow = ''
            inflow = transaction[10]
            if (transaction[14] == 'BEA') | (transaction[14] == 'RTI'):
                payee = transaction[17].split('>')[0].strip().strip('\'')
                memo = clean(transaction[17].split('>')[1].strip())
            else:
                payee = transaction[3]
                memo = clean(transaction[17])

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
                memo = clean(ba_split[2])
            elif transaction[6] == 'KN':
                payee = 'Triodos Bank N.V.'
                memo = clean(transaction[7])
            elif transaction[6] == 'GA':
                payee = 'GA'
                memo = clean(transaction[7])
            else:
                payee = transaction[4]
                memo = clean(transaction[7])
            if transaction[3] == 'Credit':
                inflow = transaction[2]
                outflow = ''
            if transaction[3] == 'Debet':
                inflow = ''
                outflow = transaction[2]
            output.append([date, payee, memo, outflow, inflow])
        return output

#Function for Memo cleaning
def clean(dirty_string):
    #Remove quotation marks
    clean_string = dirty_string.strip('\'')
    #Remove 'incasso' description
    clean_string = clean_string.strip('Europese incasso: NL-')
    #Remove leading IBAN
    clean_string = re.sub("^\D{2}\d{2}\D{3,4}\d{8,20}[\s, :]", "", clean_string)
    #Remove iDeal/incasso identification numbers
    clean_string = re.sub("^\d+\s\d+\s", "", clean_string)
    return clean_string





#Read csv
try:
    with open(input) as input_csv:

        csv_reader = csv.reader(input_csv)
        for line in csv_reader:
            transactions_input.append(line)
except:
    with open(input, encoding='latin-1') as input_csv: #encoding='latin-1'

        csv_reader = csv.reader(input_csv)
        for line in csv_reader:
            transactions_input.append(line)
print("Opening " + input)

#Check bank type
if transactions_input[0] == ['Date', 'Payee', 'Account number', 'Transaction type', 'Payment reference', 'Amount (EUR)', 'Amount (Foreign Currency)', 'Type Foreign Currency', 'Exchange Rate']:
    converter = N26Converter()
    print("N26 csv recognised")
elif transactions_input[0] == ['IBAN/BBAN', 'Munt', 'BIC', 'Volgnr', 'Datum', 'Rentedatum', 'Bedrag', 'Saldo na trn', 'Tegenrekening IBAN/BBAN', 'Naam tegenpartij', 'Naam uiteindelijke partij', 'Naam initiërende partij', 'BIC tegenpartij', 'Code', 'Batch ID', 'Transactiereferentie', 'Machtigingskenmerk', 'Incassant ID', 'Betalingskenmerk', 'Omschrijving-1', 'Omschrijving-2', 'Omschrijving-3', 'Reden retour', 'Oorspr bedrag', 'Oorspr munt', 'Koers']:
    converter = RaboConverter()
    print("Rabobank csv recognised")
elif path[0].__contains__('mutations'):
    converter = TrioConverter()
    print("Triodos csv recognised")
elif path[0].__contains__('transactie-historie'):
    converter = ASNConverter()
    print("ASN csv recognised")

#Convert
transactions_output = converter.convert(transactions_input)
print("Converted " + str(len(transactions_input)) + " transactions")

#Write YNAB csv
with open(output, 'w') as output_csv:
    csv_writer = csv.writer(output_csv)
    for transaction in transactions_output:
        csv_writer.writerow(transaction)
print("Saved YNAB csv as " + output)
