# python code to read and parse an csv file

import json

pass_count = 0
fail_count = 0

# Open JSON file (same folder as this script)
with open("api_test_results.json", "r") as f:
    content = json.load(f)   #  parses JSON into a Python dictionary
    tests  =  content["tests"]   # access/ gets the list of test cases

    for test in tests:
        if test["status"] == "PASS":
            pass_count += 1
        elif test["status"] == "FAIL":
            fail_count +=1

print(f"Pass:{pass_count}, Fail:{fail_count}")