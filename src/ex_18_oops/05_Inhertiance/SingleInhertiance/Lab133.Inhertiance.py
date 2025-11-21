#single inhertiance

class BaseTest:
    driver = "chrome"
    __driver1="FF"
    def setup(self):
        print("Base setup"+ self.__driver1)


class LoginTest(BaseTest):
    def run(self):
        self.setup()
        print("Login" +self.driver)

t=LoginTest()
t.run()