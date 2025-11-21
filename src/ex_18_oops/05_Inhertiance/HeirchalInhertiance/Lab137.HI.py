class Father():
    def fath(self):
        print("Father")

class Child1(Father):
    def gun(self):
        self.fath()
        print("Child1")

class Child2(Father):
    def run(self):
        self.fath()
        print("Child2")



c1=Child1()
c1.gun()
c2=Child2()
c2.run()
