# 6 Задание
profit = int(input('Введи выручку: '))

costs = int(input('Введи исздержки: '))

if profit > costs:
    rent = (profit - costs) / profit
    print("рентабельность выручки:" + str(rent))
    n = int(input('Введи кол-во персонала: '))
    print("прибыль фирмы в расчёте на одного сотрудника:" + str((profit - costs) / n))
else:
    print("убыток — издержки больше выручки")

