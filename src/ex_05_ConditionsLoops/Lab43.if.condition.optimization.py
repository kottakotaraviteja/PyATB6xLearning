num=int(input("Enter age").strip())

if num<=0 or num>130:
    print("Enter a valid age")
else:
    if num>=21:
      print("user can go to club")
    else:
       print("user can not go to club")