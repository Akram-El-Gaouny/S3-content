import os
import pandas as pd

# Read mappings CSV file
mappings = pd.read_excel("./Checkov Mapping.xlsx")

# getting the checkov output file
test_output = os.getenv("TEST_PATH")

# read the test report
f = open(test_output, "r")
content = f.read()
f.close()

# Adjust the content of the report to display NIST-SP-800 checks if they are available
for i in range(len(mappings)):
    if str(mappings["NIST-SP-800"][i]) != "nan":
        content = content.replace(mappings["CHECKOV_CODE"][i], str(mappings["NIST-SP-800"][i]))

# write to the file
f = open(test_output, "w")
f.write(content)
f.close()

# Inform user that the file has been updated
print("File Updated!")