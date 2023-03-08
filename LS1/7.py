km1 = int(input('Введи в 1 день: '))
km2 = int(input('Введи в искомый день: '))

day = 1
while km1 <= km2:
    print(f'{day}-й день: {km1}')
    km1 = km1 * 1.1
    day = day + 1
print(f'{day}-й день: {km1}')
print("Ответ:" + str(day))
