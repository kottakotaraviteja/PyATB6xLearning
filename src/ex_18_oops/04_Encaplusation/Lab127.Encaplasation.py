
class Car:

    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year


    def Car_engine(self):
        print("Name of the car:"+self.name)
        print("Model of the car:"+self.model)
        print("Year of the car:"+self.year)

Ferrari=Car("Ferrari", "M", "1999")
Ferrari.Car_engine()

mg_hector=Car("Mg_Hector", "M", "2011")
mg_hector.Car_engine()