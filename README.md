# Triodos2YNAB
Convert Triodos transaction csv's to a YNAB-supported format

## Usage

1. Install [Python 3](https://www.python.org/)
2. Download transactions from [Triodos](https://www.triodos.nl/veelgestelde-vragen/hoe-download-ik-een-overzicht-van-mijn-bij-en-afschrijvingen-in-mijn-boekhoudprogramma?id=126d202a2cba) as csv file 
3. Convert using:
```
    python3 trio2ynab.py mutationsXXXXXXX.csv
```
4. The converted .csv will be in the same directory as the original one, and you are ready to upload to YNAB!
