class Bank:

     def __init__(self,account_number,balance):
         self.__account_number=account_number
         self.balance=balance

     def check_balance(self):
         print(self.balance)

     def deposit(self,amount):
         self.balance=self.balance+amount

     def show_me_account_number(self,is_auth):

         if is_auth==True:
             print(self.__account_number)
         else:
             print("Not allowed")
icici=Bank(123456789,100)
icici.deposit(300)
icici.check_balance()
icici.show_me_account_number(True)