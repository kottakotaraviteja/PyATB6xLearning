#Hybrid Inhertiance

#A mix of multiplelevel and multiple inhertiance
#mixture of multiple type of inhertiance

class A():
    def alpha(self):
        print("alpha")

class B():
    def beta(self):
        print("beta")

class C(A,B):
    def run(self):
        print("C")

class D(C):
    def run1(self):
        self.alpha()
        self.beta()
        self.run()
        print("D")

d=D()
d.run1()






