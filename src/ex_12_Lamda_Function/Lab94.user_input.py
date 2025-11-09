user_input = int(input("Enter a number"))

lamb_function= lambda num:"even" if num%2==0 else "odd"
result=lamb_function(user_input)
print(result)