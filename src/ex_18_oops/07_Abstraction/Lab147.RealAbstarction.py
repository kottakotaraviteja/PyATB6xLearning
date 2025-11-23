from abc import ABC,abstractmethod

class Browser(ABC):
    @abstractmethod
    def open(self):
        pass

    def close(self):
        print("Stop")

class Chrome(Browser):
    def open(self):
        print("Open Chrome browser")
        

c=Chrome()
c.open()
c.close()
