numbers=[1,2,3,4,5,6,7,8,9]

def even_number(x):
    return x%2==0

even=list(filter(even_number,numbers))
print(even)