class Car:
    def __init__(self, model: str, color: str):
        self.model = model
        self.color = color
        print(f"Model: {self.model}, Color: {self.color}")
    
    def __str__(self):
        return f'{self.color} {self.model}'
    
    def __repr__(self):
        return f'Car(model={self.model}, color={self.color})'
        
if __name__ == "__main__":
    car = Car("Toyota", "red")
    print(car)  # Output: red Toyota
    print(car.__repr__())  # Output: Car(model=Toyota, color=red)