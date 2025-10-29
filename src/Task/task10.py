#Factrioal number

num = int(input("Enter a number for which factorial you want"))

factorial = 1

if num<0:
    print("Invalid input")

if num == 0:
    print("Fact= ", factorial)
else:
    for i in range(1,num+1):

        factorial=factorial*i

print("Fact of: ",factorial)







