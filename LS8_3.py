class NotNumber(Exception):
    def __init__(self, txt):
        self.txt = txt

my_list = []
while True:
    try:
        value = input('Введите число в список:')
        if value == 'q':
            break
        if not value.isdigit():
            raise NotNumber(value)
        my_list.append(int(value))
    except NotNumber as ex:
        print('Не число!', ex)
print(my_list)