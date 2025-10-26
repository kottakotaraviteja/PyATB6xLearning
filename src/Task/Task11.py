"""
response=int(input("Enter your response:"))

attempt =1


if response==200:
    print("✅ Test Passed")
else:
    while attempt<3:
     response = int(input("Enter correct response"))
     if response==200:
        print("Test Passed")
        attempt = attempt + 1
     else:
        attempt = attempt + 1
        print("Test Failed")
"""
response_code = int(input("Enter response Code: "))
if response_code == 200:
    print(f"The response code is {response_code}\n"
          f"✅ Test Passed")
else:
    i = 1
    print("Response code not matched.\n"
          "Reattempting start.........")
    while response_code != 200 and i < 3:

        if response_code == 200:
            print(f"The response code is {response_code}\n"
                  f"✅ Test Passed")
        else:
            print(f"Attempt {i} failed: Response {response_code}")
            print("-" * 100)
            i = i + 1
            response_code = int(input("Enter response code again: "))


    if response_code == 200:
        print(f"The response code is {response_code}\n"
              f"✅ Test Passed")
    else:
        print(f"All the 3 attempts failed.\n"
              f"❌ Test Failed")











