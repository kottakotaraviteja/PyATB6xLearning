"""
An API sometimes fails due to network delays.

Write a program to retry the API call 3 times until the response code becomes 200.

If it still fails after 3 tries, print a failure message.

Hint: Use a while loop with a counter.
Hint: Use a while loop with a counter.

Expected Output Example:

Attempt 1: Response 500

Attempt 2: Response 200

✅ Test Passed
"""

Attempt=1
max_attempts = 3
response = None

while Attempt <=max_attempts:
    response = int(input("Enter Response Code: "))
    if response == 200:
      print("Test Passed")
      break
    else:
       Attempt=Attempt + 1

if response!=200:
    print("Test Failed attempt Three")


