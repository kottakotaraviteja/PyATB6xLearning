class GrandFather:
    def gfather(self):
        print("GrandFather money")

class Father(GrandFather):
    def father(self):
        print("Father money")

class Child(Father):
    def run(self):
        self.gfather()
        self.father()
        print("Child money")

c=Child()
c.run()
