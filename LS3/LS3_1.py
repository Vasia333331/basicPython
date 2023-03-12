def div(*args):

    try:
        arg1 = int(input("Введи делимое "))
        arg2 = int(input("Введи делитель "))
        res = arg1 / arg2
    except ValueError:
        return 'Вводить надо было числа'
    except ZeroDivisionError:
        return "Нельзя делить на 0"

    return res

print(f'Результат  {div()}')