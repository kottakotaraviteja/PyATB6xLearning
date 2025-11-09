"""
a={1,2,3,4}
b={3,4,5}

#print(a.union(b))

print(a|b)

#print(a&b)

print(a.intersection(b))

print(a-b) #difference

print(b-a)

print(a^b) #symetric difference
"""

set1={1,2,3}
set2={4,5,6}

print(set1.union(set2))

set3={1,2,3,4,5}
set4={4,5,6,7,8}

print(set3.intersection(set4))

print(set3-set4)

print(set4-set3)