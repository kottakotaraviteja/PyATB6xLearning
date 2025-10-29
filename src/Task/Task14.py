#Skip numbers divisible by 3, from (0,100)

for i in range(1,100,1):

    if(i%3==0):
        continue
    else:
        print(i)