

try:
    a = int(input("Enter number1:"))
    b = int(input("Enter number2:"))
    c=a/b

except ZeroDivisionError:
    print("Error ZeroDivisionError")
except ValueError:
    print("ValueError")
else: #runs only we try is passed
    print(c)
finally:
    print("I will execute")