sample_list = []

for i in range(10):
    if i % 2 == 0:
        sample_list.append(i)
    
print(sample_list)


# List Comprehension

sample_list2 = [i*2 for i in range(10) if i % 2 == 0] 

print(sample_list2)