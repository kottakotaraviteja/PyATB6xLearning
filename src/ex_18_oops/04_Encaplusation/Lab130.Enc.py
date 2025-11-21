class Car:

    def __init__(self):
        self.password = "1234"
        self.__password_private="admin"

    def nany(self):
         self.__password_private="5678"

object_ref=Car()
object_ref.nany()
print(object_ref.password)
#print(object_ref.__password)
