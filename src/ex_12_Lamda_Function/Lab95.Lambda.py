import math

num=int(input("Enter a number: "))
lambda_fun= lambda num: math.pow(num,2)

result=lambda_fun(num)
print(result)