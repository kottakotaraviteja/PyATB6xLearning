class InvalidException(Exception):
    pass

def you_can_drink(age):
    if age <18:
        raise InvalidException("You can't drink.")
    
print(you_can_drink(19))

