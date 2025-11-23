from abc import ABC, abstractmethod
class Father:

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def loan(self):
        pass

class son(Father):

    def loan(self):
        print("Loan of 50k")

S=son("Amit")
S.loan()
