numbers=[1234,4567,8901]

def mil_sec(x):
    return x/1000

mil=list(map(mil_sec,numbers))
print(mil)