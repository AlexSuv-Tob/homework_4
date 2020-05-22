my_list = [1, 5, 4, 5, 6, 8, 9, 8]
new_list = [j for i, j in zip(my_list, my_list[1:]) if j > i]
print(new_list)