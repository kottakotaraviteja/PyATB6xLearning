#problem to find the grades

#Marks range 90 to 100 - grade A
#Marks range 80 to 90 - grade B
#Marks range 70 to 80 - grade c
#Marks range 60 to 70- grade d
#Marks range 50 to 60 -grade f

marks =int(input("Enter marks: "))

if marks<=0 or marks>100:
    print("your a super man no garde ")
else:
    if marks>= 90 and marks<=100:
       print("Grade A")
    elif marks>= 80 and marks<90:
       print("Grade B")
    elif marks>= 70 and marks<80:
     print("Grade C")
    elif marks>= 60 and marks<70:
     print("Grade D")
    else:
     print("Grade f")



