class Fruit:
    def __init__(self, name: str, calories: int):
        self.name = name
        self.calories = calories
        
    def explaod(self):
        print(self.name, 'expload!')
        
    def eat(self):
        print(self.name, 'has been eaten')
        
def hello():
    print('Hello!')

hello()
# eat()  throw an error because eat is not defined in the global scope

# to call the eat method, we need to create an instance of the Fruit class

Fruit('Apple', 95).eat()  # Output: Apple has been eaten