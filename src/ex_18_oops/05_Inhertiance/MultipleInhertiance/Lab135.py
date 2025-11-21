class Father1:
    def money(self):
        print("Money Father1")

class Father2:
    def money(self):
        print("Money Father2")

class Son(Father1, Father2):
    def run(self):
        self.money()
        print("Son want money")

c=Son()
c.run()



