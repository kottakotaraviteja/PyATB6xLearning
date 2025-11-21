class person:

    #attributes
    name="none"
    id="none"
    age="none"
    email="none"

    #methods
    # self - self will be first arugemenet
    def Talk(self):
        print("I am talking")

    def Walk(self):
        print("I am walking")
    def Read(self):
        print("I am reading")

    def Sleep(self):
        print("I am sleeping")

    def sleep2(name):
        print(name , "I am sleeping")

#object is instance of class

ravi=person()
print(ravi.name)
ravi.Walk()
ravi.Read()