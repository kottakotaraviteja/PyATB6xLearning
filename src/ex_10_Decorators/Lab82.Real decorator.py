def Run(func):

    def wrapper():
        print("Before running the test")
        func()
        print("After running the test")

    return wrapper()
@Run
def log_1():
    print("Time taken to run the log one")
@Run
def log_2():
    print("Time taken to run the log two")