number: list[int] = list(range(21))

print(number[::3])     # jump by 3

print(number[10::3])   # Start at 10 and jump by 3

print(number[10:18:2]) # Start at 10 and end at 18 and jump by 2

print(number[10:])     # Start at 10 and end at the end

print(number[:10])     # Start at the beginning and end at 10