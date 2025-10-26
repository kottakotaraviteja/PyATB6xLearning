num =int(input("enter num:"))

fact=1

if num<0:
    print("Please enter a positive number")
elif num==0:
    print("Factrioal of 0 is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("Fact of num:",fact)


