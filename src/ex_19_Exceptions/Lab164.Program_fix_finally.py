

try:
    a = int(input("Enter number1:"))
    b = int(input("Enter number2:"))
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Error ZeroDivisionError")
except ValueError:
    print("ValueError")
finally:
    print("I will execute")