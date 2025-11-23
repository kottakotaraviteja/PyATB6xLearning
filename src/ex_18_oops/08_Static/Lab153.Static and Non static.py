class Math:

    def divide(self,a,b):

        return a/b


    @staticmethod
    def multiply(a,b):
        return a*b

m=Math()
print(m.divide(2,3))
print(Math.multiply(2,3))

#static methods dont need object