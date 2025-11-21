class Dog():

    name="none"
    breed="none"
    height="none"
    weight="none"

    def __init__(self):
        print("I will be called")

    def bark(self):
        print("barking")

    def sleep(self):
        print("sleeping",self.name)

    def talk(self):
        pass

chow_ref=Dog()

mow_ref=Dog()

print(chow_ref.name)
print(mow_ref.name)