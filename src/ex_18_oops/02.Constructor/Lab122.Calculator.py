class Calculator:

    def __init__(self):
      print("DC")

    def sum(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b

a=float(input("Enter a number: "))
b=float(input("Enter another number: "))

c=Calculator()
print("sum of a and b",c.sum(a,b))
print("sub of a and b",c.sub(a,b))
print("mul of a and b",c.mul(a,b))
print("div of a and b",c.div(a,b))


