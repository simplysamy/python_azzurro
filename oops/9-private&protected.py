class Lamp: 
    def __init__(self, name: str, model: int):
        self.name = name
        self.__model = model
    
    def description(self):
        print(self.name, self.__model)
        
lamp: Lamp = Lamp('Desk Lamp', 2021)
lamp.description()

# print(lamp.__model)  # This will raise an AttributeError since __model is private
print(lamp._Lamp__model)  # This will work, but it's not recommended to access private attributes directly