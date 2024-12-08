from enum import Enum

# Checkfing the sate of the light lamp
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'
    
color = Color.GREEN

if color == Color.RED:
    # print('The color is red')
    print(f'The color is', color.value) # get the value
elif color == Color.GREEN:
    print(f'The color is', color.name)  # get the name
elif color == Color.BLUE:
    print('The color is blue')

