class Car:
    def __init__(self, model: str, color: str):
        self.model = model
        self.color = color
        print(f"Model: {self.model}, Color: {self.color}")
    
    def __str__(self):
        return f'{self.color} {self.model}'
        
if __name__ == "__main__":
    car1 = Car("Toyota", "red")
    print(car1)  # Output: red Toyota