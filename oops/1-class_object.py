class Car:
    def __init__(self, model: str, color: str):
        self.model = model
        self.color = color
        print(f"Model: {self.model}, Color: {self.color}")
    
    def drive(self):
        print(f"The {self.color} {self.model} is driving.")
        
if __name__ == "__main__":
    car1 = Car("Toyota", "red")
    car1.drive()