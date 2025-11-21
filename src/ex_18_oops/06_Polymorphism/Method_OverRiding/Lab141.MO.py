class BaseTest():
    def run(self):
        print("BaseTest")

class BrowserTest(BaseTest):
    def run(self):
        print("BrowserTest")

class LoginTest(BrowserTest):
    def run(self):
        print("LoginTest")

class APITest(LoginTest):
    def run(self):
        print("APITest")

r=BaseTest()
r.run()