def add_security(func):

    def wrapper():
        print("1.Before the function called")
        print("2.Add helemet, dashcam,licence,RC Book")
        func()
        print("3.After the function called")
        print("4.Secure driving leave all items")

    return wrapper()

@add_security
def drive_ola_scooter():
    print("I am driving ola scooter")

@add_security
def scotter_driving():
    print("I am driving scotter")