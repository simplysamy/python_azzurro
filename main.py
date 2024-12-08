from enum import Enum

# Checkfing the sate of the light lamp
class state(Enum):
    OFF = 0
    ON = 1

state_of_lamp = state.OFF

if state_of_lamp == state.ON:
    print("The lamp is on")
else:
    print("The lamp is off")

