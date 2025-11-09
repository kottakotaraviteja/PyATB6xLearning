#set is a unique collection
#{}
list_of_unique_ele={1,2,2,3,4,5}
print(list_of_unique_ele)

list=[1,1,2,2,3,4,5]
list1=set(list)
print(list1)


tuple=(1,2,3,4,4,5,5)
list2=set(tuple)
print(list2)

set={1,"ravi",'a'}
print(set)

#empty = set()
#print(type(empty))

for item in set:
    print(item)

set.add("teja")
print(set)
