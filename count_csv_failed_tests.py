# python to find or count tests failed in a csv file

#
import csv
counter = 0 # initialize counter

# use a full path sice the tests csv files are in the downloads folder
with open("C:/Users/mirdo/Downloads/test_results.csv - Sheet1.csv", "r") as file:
    testfailed = csv.DictReader(file)
    for row in testfailed:
        if row["status"].strip().lower() == "fail": # compare it
# To make my CSV validation more robust, I normalize values using .strip().lower() before comparison."
            counter += 1 # increment the counter

    # print total failed tests after counting
    print(f"Number of failed rows: {counter}")
