my_list=[1,2,3]

my_list[0]="ravi"
my_list[1]="teja"

for item in my_list:
    print(item)

my_list1=[1,2,3]

 #indexing

print(my_list1[0])
print(my_list1[1])
print(my_list1[2])


#append - append object to the end of the list

my_list1.append(6)
print(my_list1)

my_list1.append(7)
print(my_list1)

#extend
my_list1.extend([10,11,12])
print(my_list1)

#insert
my_list1.insert(1,"ravi")
print(my_list1)

my_list1.insert(2,"teja")

my_list1[1]="new"
print(my_list1)

print(len(my_list1))

my_list1.remove("new")
print(my_list1)

print(len(my_list1))

my_copy_list=my_list1.copy()
print(my_copy_list)

my_copy_list.remove("teja")
print(my_copy_list)
print(my_list1)