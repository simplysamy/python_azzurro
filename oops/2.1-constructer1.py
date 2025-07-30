class Fruit:
    def __init__(self, name: str):
        self.name = name
        self.letter_count = len(name)
        print('Constructer called')
        
fruit: Fruit = Fruit("Banana")
print(fruit.name) 
print(fruit.letter_count)  # Output: 6