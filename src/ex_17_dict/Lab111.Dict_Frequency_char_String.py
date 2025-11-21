#frequency of character in string
#write a program to count the frequency
#of each character in a string

String=input("Enter a String\n")

Char_Count={}

for char in String:
    Char_Count[char]=Char_Count.get(char,0)+1

print(Char_Count)