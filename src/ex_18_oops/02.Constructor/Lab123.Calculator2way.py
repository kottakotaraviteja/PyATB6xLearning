class calc:

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b


c=calc(1,2)
print(c.add(3,4))
print(c.sub(3,4))
print(c.mul(3,4))
print(c.div(3,4))
