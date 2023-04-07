
from math import factorial


def fact(n: int):
    for i in range(1, n + 1):
        yield factorial(i)

input_data = input('Пожалуйста введите количество вычисленных факториалов: ')

value = int(input_data)

for el in fact(value):
    print(el)
