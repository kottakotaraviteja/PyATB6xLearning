class BaseTest:
    def run(self):
        print("Run Generic Test")

class LoginTest(BaseTest):
    def run(self):
        print("Run Login Test")

l=BaseTest()
l.run()