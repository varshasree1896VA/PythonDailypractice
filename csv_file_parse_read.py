# python code to read and parse an csv file

import csv

# Use the full path because the CSV is in Downloads
with open("C:/Users/mirdo/Downloads/test_results.csv - Sheet1.csv", "r",newline="") as f:
    testfile = csv.DictReader(f)
    for row in testfile:
        if row['status'] == 'FAIL':
            print(row['id'], row['test_name'])

