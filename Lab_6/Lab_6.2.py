class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"\nНазвание модели: {self.make}, \nМодель: {self.model}\n"
    

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model) 
        self.fuel_type = fuel_type

    def get_info(self):
        return f"Название модели: {self.make}, \nМодель: {self.model}, \nТип топлива: {self.fuel_type}\n"
    
mashina1 = Vehicle("toyota", "camry3.5")
print(mashina1.get_info())
mashina2 = Car("toyota", "camry 3.5", "dizel")
print(mashina2.get_info())