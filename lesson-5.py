'''
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''

my_func = open('text.txt', 'w')
line = input('Введите текст \n')
while line:
    my_func.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break
my_func.close()

my_func = open('text.txt', 'r')
content = my_func.readline()
print(content)
my_func.close()

'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, 
выполнить подсчет количества строк, количества слов в каждой строке.
'''
my_fail = open('Text_1.txt', 'r')
content = my_fail.read()
print(f'Содержание файла: \n {content}')
my_file = open('Text_1.txt', 'r')
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')
my_file = open('Text_1.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'Окличество символов {i + 1} - ой строки {len(content[i])}')
my_file = open('Text_1.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_file.close()

'''
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. 
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. 
Выполнить подсчет средней величины дохода сотрудников.
'''
with open('list.txt', 'r') as my_file:
    max = []
    min = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           min.append(i[0])
        max.append(i[1])
print(f'Оклад меньше 20.000 {min}, средний оклад {sum(map(int, max)) / len(max)}')
