a = 10
b = 1 * a

print (id(a))
print (id(b))

print(a is b) # TRUE

a = 10.0
b = 1.0 * a

print (id(a)) # Both a & b have different memory address
print (id(b))  

print(a is b) # FALSE

print(a is not b) # TRUE


