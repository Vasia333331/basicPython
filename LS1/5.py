# 5 Задание
profit = int(input('Введи выручку: '))

costs = int(input('Введи исздержки: '))

if profit == costs:
    print("нет не прибыли ни убытков")
elif profit > costs :
    print("прибыль — выручка больше издержек")
else:
    print("убыток — издержки больше выручки")

