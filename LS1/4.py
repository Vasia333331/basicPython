# 4 Задание

n = int(input('Введи число: '))
r=-1
while n > 0:
    d = n % 10
    n //= 10
    if d > r:
        r = d
print(r)


