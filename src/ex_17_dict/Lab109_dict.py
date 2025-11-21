key=["Name","Role","Experience"]
value=["Ravi","SDQET","3"]


my_dict=dict(zip(key,value))
print(my_dict)

#merg dict

dict1={"a":1,"b":2,"c":3}
dict2={"d":4,"e":5,"f":6}

mergr=  dict1 | dict2
print(mergr)
print(mergr.get("a"))