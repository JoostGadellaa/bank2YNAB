# Triodos2YNAB
Convert Triodos transaction csv's to a YNAB-supported format

## Usage

1. Install [Python 3](https://www.python.org/)
2. Download the csv file from [Triodos](https://www.triodos.nl/veelgestelde-vragen/hoe-download-ik-een-overzicht-van-mijn-bij-en-afschrijvingen-in-mijn-boekhoudprogramma?id=126d202a2cba)
3. Convert using:
```
    python3 trio2ynab.py mutationsXXXXXXX.csv
```
Make sure you are either in the directory where both the script and the .csv file are, or link the full path of both the script and mutations file. E.g.:
```
    python3 /Users/joostgadellaa/Documents/Triodos2YNAB-master/trio2ynab.py /Users/joostgadellaa/Downloads/mutations20200500000000.csv 
```

4. The converted .csv will be in the same directory as the original one, and you are ready to upload to YNAB!
