
class TestExample:

    def __init__(self):
        self.driver="chrome"
        self._config="stage"
        self.__api__key="ABC12345"

    def show(self):
        print(f"Driver: {self.driver}")
        print(f"Config: {self._config}")
        print(f"APIKey: {self.__api__key}")

obj=TestExample()
obj.show()