from abc import ABC,abstractmethod

class Gearbox(ABC):

    @abstractmethod
    def gear(self):
        pass

class Engine:
    @abstractmethod
    def engine(self):
        pass
    @abstractmethod
    def box(self):
        pass

class car(Gearbox,Engine):
    def gear(self):
        print("Gear")

    def engine(self):
        print("Engine")

    def box(self):
        print("Box")

    def drive(self):
        self.gear()
        self.engine()
        self.box()




C=car()
C.drive()
