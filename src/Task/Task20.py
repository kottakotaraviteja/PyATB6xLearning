#Question - ✅ Count vowels and consonants in a String

name=input("Enter your name:")

Vouwles="aeiouAEIOU"

count=0
for c in name:
     if c in Vouwles:
         count=count+1

print("vouwles:",count)

count1=0

for b in name:
    if b not in Vouwles:
        count1=count1+1

print("Constants:",count1)
