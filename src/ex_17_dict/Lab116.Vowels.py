String="Hello World"

vowles="aeiou"
vowle_count=0

result=list()

for char in String:
    if char in vowles:
        vowle_count=vowle_count+1
        result.append(char)

print(result)