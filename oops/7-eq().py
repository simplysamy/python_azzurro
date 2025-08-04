class Fruit:
    def __init__(self, name: str, calories: int):
        self.name = name
        self.calories = calories
        
    def __eq__(self, other):
        return self.name == other.name
        
if __name__ == "__main__":
    fruit1 = Fruit("Apple", 95)
    fruit2 = Fruit("Apple", 50)

    
    # Checking equality based on name 
    print(fruit1 == fruit2)  # Output: True
