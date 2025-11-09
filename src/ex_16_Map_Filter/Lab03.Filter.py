from operator import truediv

names=["QA","","Automation",""]


def none(x):
    if x !="":
      return True
    return None


empty=list(filter(none,names))
print(empty)