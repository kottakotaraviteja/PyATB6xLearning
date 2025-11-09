my_dict={

    "name":"Ravi",
    "age":22,
    "height":70,
    "weight":80,
    "eye_color":"Black"
}
print(my_dict)
print(my_dict["name"])
print(my_dict["age"])
print(my_dict["height"])

my_dict["height"]=100
print(my_dict)

del my_dict["height"]
print(my_dict)

#for key, in my_dict.items():
   # print(key, value)

print("name" in my_dict)