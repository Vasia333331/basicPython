# 2 Задание
seconds = int(input('Введи число: '))

hour = seconds // 3600

seconds1 = seconds % 3600

minutes = seconds1 // 60

seconds = seconds % 60

print(f'{hour:02}:{minutes:02}:{seconds:02}')

