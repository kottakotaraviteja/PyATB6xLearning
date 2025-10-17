#I/P response = 404 , O/P ❌ Failed API Request
#I/P response = 200 , O/P ✅ Passed API Request

response =int(input("Enter Input"))
if response==200:
    print("✅ Passed API Request")
else:
    print("❌ Failed API Request")