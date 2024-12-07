# old approach for reading a file

# file = open("sample.txt")
# text = file.read()
# file.close()

with open("sample.txt") as file:
    text = file.read()

print(text)