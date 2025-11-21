class Person:

    def __init__(self):
        print("Please enter the user details : Name,Age,phone,occupation,")
        self.name=input("Please enter your name: ")
        self.age=input("Please enter your age: ")
        self.occupation=input("Please enter your occupation: ")
        self.phone=input("Please enter your phone number: ")
    def display_details(self):
        print("name is:",self.name,"Age is:",self.age,"phone is:",self.phone,"occupation is:",self.occupation)



ravi=Person()
ravi.display_details()
