#find the given postive number is even or odd

num =int(input("Enter a number").strip())
"""
if num>0:
   if num%2==0:
    print("Even")
   else:
    print("Odd")
else:
   print("Given number is negative")
"""
print("given number is even" if num%2==0 else "given number is odd")