from itertools import count
from itertools import cycle

for el in count(int(input('Введите стартовое число '))):
    if el > 10:
        break
    else:
        print(el)

count = 0
my_list = [True, 'ABC', 123, None]
for el in cycle(my_list):
    if count > 10:
        break
    else:
        print(el)
        count +=1