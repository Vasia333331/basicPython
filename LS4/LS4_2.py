my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f'Исходный список {my_list}')
my_new_list = [my_list[el] for el in range(1, len(my_list)) if my_list[el] > my_list[el-1]]
print(f'Новый список {my_new_list}')
"""my_new_list = []
for el in range(1, len(my_list)):
   if my_list[el] > my_list[el-1]:
        my_new_list.append(my_list[el])"""
print(f'Новый список {my_new_list}')
