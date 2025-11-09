def before_and_after_testing(func):

    def wrapper():
        print(" before testing")
        func()
        print(" after testing")
    return wrapper()

@before_and_after_testing
def Ui_Testing():
    print("I am doing UI Testing")