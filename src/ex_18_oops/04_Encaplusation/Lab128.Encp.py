

class Login_page:



    def log_details(self,username_args,password_args):
           self.username = username_args
           self.password = password_args


    def login(self):
        if self.username=="admin" and self.password=="1234":
            print("Login Successful")
        else:
            print("Login Failed")


username=input("Enter Username:")
password=input("Enter Password:")

login_reference=Login_page(username,password)
login_reference.login()
