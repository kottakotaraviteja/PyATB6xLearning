"""
*
**
***
****
*****
"""

#for i in range(1,6):
 #   print('*' *i)


#for j in range(5,0,-1) :
 #   print('*' *j)

n=int(input("Enter a number") )

for i in range(1,n+1):
    for j in range(1,i+1):
       print('*',end=" ")
    print()

