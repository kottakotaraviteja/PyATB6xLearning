#Create a program to sum of the three numbers from the user input
#if user dont enter any number, use default as 100,200, 300

num1=int(input("Enter the first number\n"))
num2=int(input("Enter the second number\n"))
num3=int(input("Enter the third number\n"))

def sum_of_numbers(num1=100,num2=200,num3=300):
    return num1+num2+num3

result=sum_of_numbers(num1,num2,num3)
result1=sum_of_numbers()
result2=sum_of_numbers(num1=20,num3=30)
result3=sum_of_numbers(num1=20,num2=40)
print(result)
print(result1)
print(result2)