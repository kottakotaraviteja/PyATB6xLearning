from abc import ABC,abstractmethod

class ExcelReader(ABC):
    @abstractmethod
    def Read(self):
        pass

class Browser(ExcelReader):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def write(self):
        pass


class TC(Browser):

    def Read(self):
        print("Read")

    def open(self):
        print("Open")

    def write(self):
        print("Write")

    def drive(self):
        self.Read()
        self.open()
        self.write()


t=TC()
t.drive()






