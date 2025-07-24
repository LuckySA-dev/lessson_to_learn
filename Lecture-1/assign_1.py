input_list = [1, 2, 3, 4, 5, 1, 2, 3]
my_list = []

for i in input_list:
    if i not in my_list:
        my_list.append(i)
        
print(my_list)
