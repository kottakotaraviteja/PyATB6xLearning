# find the first non repeating char in the string using set
from itertools import count

#swiss - s - wrong - w - answer


print("swiss".count("s"))
print("swiss".count("w"))


def non_repeating_function(String):
    for char in String:
        if  String.count(char)==1:
            return char
    return None

print(non_repeating_function("swiss"))
print(non_repeating_function("anniusha"))