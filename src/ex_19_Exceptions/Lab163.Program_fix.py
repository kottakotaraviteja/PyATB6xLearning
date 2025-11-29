a=int(input("Enter number1:"))
b=int(input("Enter number2:"))

try:
  c=(a/b)
  print(c)
except ZeroDivisionError:
    print("Error ZeroDivisionError")

except ValueError:
    print("Error ValueError")

