class Dog:

    name="none"
    breed="none"
    height="none"
    weight="none"
    race="none"

    def __init__(self,name,bread):
        print("Paratemetrized constructor")
        self.name=name
        self.breed=bread
    def bar(self):
        print("barking")

    def sleep(self):
        print("who is sleep",self.name)

    def talk(self):
        pass

chow=Dog("chow","goat")

bow=Dog("bow","geee")

chow.sleep()

bow.sleep()

chow.bar()
