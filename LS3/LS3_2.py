def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func(surname='Иванов', name='Иван', year='1995', city='Мытищи', email='asddas@mail.ru',
              telephone='8-800-555-35-35'))