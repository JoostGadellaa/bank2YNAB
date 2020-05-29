import sys
import csv

bestandslocatie = sys.argv[1]

with open(bestandslocatie) as triodos_csv:
    print(triodos_csv.readline())
