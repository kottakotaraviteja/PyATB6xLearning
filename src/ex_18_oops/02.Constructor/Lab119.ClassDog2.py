print("outside the class")

class Phone:

    model="none"


    def __init__(self):
        print("DC")
    def talk(self):
        print("talking")

iphone=Phone()
iphone.talk()

print("outside the class2")