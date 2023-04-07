with open('sal.txt', 'r') as my_file:
    sal = []
    poor = []

    my_list = my_file.read().split('\n')
    my_file.close()

    for i in my_list:
        if i == "" : #отсекаем пустые строки вконце
            break
        else:
            i = i.split()
            if int(i[1]) < 20000:
                poor.append(i[0])
            sal.append(float(i[1]))
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(sal) / len(sal)}')