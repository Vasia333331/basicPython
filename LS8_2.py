class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

try:
    delimoe = int(input("Введите положительное число: "))
    delitel= int(input("Введите положительное число: "))
    if delitel == 0:
        raise OwnError("Деление на ноль!")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Все хорошо. Деление: {delimoe / delitel}")