class BaseTest:
    def __init__(self,browser):
        self.browser = browser


    def setup(self):
        print(f"Launching {self.browser}")



class LoginTest(BaseTest):
    def run1(self):
        self.setup()
        print("D")


class E(BaseTest):
    def run2(self):
        self.setup()
        print("E")

d=LoginTest("chrome")
d.run1()

d=LoginTest("firefox")
d.run1()



