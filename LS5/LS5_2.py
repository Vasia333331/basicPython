"""my_file = open('file_2.txt', 'r')
content = my_file.read()
print(f'Содержимое файла: \n {content}')
#my_file = open('file_2.txt', 'r')
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')
#my_file = open('file_2.txt', 'r')
content = my_file.readlines()


for i in range(len(content)):
    print(f'Окличество символов {i + 1} - ой строки {len(content[i])}')
my_file = open('file_2.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
"""
file = open('file_2.txt')

lines = 0
words = 0
symbols = 0
i=1
for line in file:
    lines += 1
    words += len(line.split())
    symbols += len(line.strip('\n'))
    print(f"В {i} строчке - {len(line.split())} слов")
    i+=1
print("В файле строчек:", lines)
print("В файле слов:", words)
print("В файле символов:", symbols)
file.close()