class Person:

    def name(self,name):
        print("Hi,",name)

    def name(self,name,lastname="sena"):
        print("Hi,",name,lastname)

p=Person()
p.name("John")