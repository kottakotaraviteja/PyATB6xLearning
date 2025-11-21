class Home:

   def __int__(self):
         self.public_var="daddy"
         self._protected_var="brother"
         self.__private_var="baby"

   def mom(self):
        print(self.mom)
        self.__wife()

   def __wife(self):
        print("private wife")

   @property
   def protected_var(self):
       return self._protected_var


family_ref=Home()
print(family_ref.protected_var)
#protected technical accessed but not recommend
family_ref.mom()
