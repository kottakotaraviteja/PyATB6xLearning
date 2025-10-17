"""
In automation, you often compare expected and actual outputs.
Write code to check if a test case passed or failed.

expected_title = "Dashboard"
actual_title = "Dashboard "

✅ Test Passed – Title matches


True - why >  Strip and convert them into the lowercase = both of them are equal.
"""

expected_title = str(input("Enter Expected Title: "))
actual_title = str(input("Enter Actual Title: "))

if expected_title.lower().strip() == actual_title.lower().strip():
    print("✅ Test Passed - Title matches")
else:
    print("Test Failed - Title does not match")