"""
print number 1 to 10
if number divides by 3 print Fizz
if number divides by 5 print Buzz
if number divides by 3 and 5 print FizzBuzz
"""
for i in range(1,101):
    if i % 3==0 and i %5==0:
        print("FizzBuzz")
    elif i % 3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)