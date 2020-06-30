# bank2YNAB
Automatically convert your bank's transaction csv's to a YNAB-supported format. Currently supports N26 and Triodos Bank.

## Usage

1. Install [Python 3](https://www.python.org/)
2. Download the csv file from [N26](https://support.n26.com/en-de/payments-transfers-and-withdrawals/balance-and-limits/how-to-export-a-list-of-my-transactions) or [Triodos](https://www.triodos.nl/veelgestelde-vragen/hoe-download-ik-een-overzicht-van-mijn-bij-en-afschrijvingen-in-mijn-boekhoudprogramma?id=126d202a2cba) 
3. Convert using:
```
    python3 bank2YNAB.py 20200600000000.csv
```
Make sure you are either in the directory where both the script and the .csv file are, or link the full path of both the script and mutations file. E.g.:
```
    python3 /Users/joostgadellaa/Documents/bank2YNAB-master/bank2ynab.py /Users/joostgadellaa/Downloads/20200600000000.csv
```

4. The converted .csv will be in the same directory as the original one, and you are ready to upload to YNAB!
