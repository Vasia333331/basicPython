from sys import argv

f_obj, name, time, salary, bonus = argv

def calculate_saalery(name, time, salary, bonus):
    try:
        time = int(time)
        salary = int(salary)
        bonus = int(bonus)
        res = time * salary + bonus
        print(f" Сотрудник {name} заработная плата сотрудника  {res}" )
    except ValueError:
        print('Вы ввели не число')

calculate_saalery(name, time, salary, bonus)