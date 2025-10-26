print("Enter the type of the test you want to run")
test_type=input("Type the test you want to run  API, UI,Performance, Security: ")

match test_type:

    case "API":
        print("We are running Postman testing")
    case "UI":
        print("We are running Selenium testing")
    case "Performance":
        print("We are running Performance testing")
    case "Security":
        print("We are running Security testing")
    case _:
        print("Invalid input")
