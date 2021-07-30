'''
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
'''

list_1 = [2, 'text', True, 2.3, None]

for el in range(len(list_1)):
    print(type(list_1[el]))

'''
2. Для списка реализовать обмен значений соседних элементов, т.е. 
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. 
При нечетном количестве элементов последний сохранить на своем месте. 
Для заполнения списка элементов необходимо использовать функцию input().
'''

my_list = ['a', 'b', 'c', 'd', 'e']
print(my_list)
if len(my_list) % 2 == 0:
    i = 0
    while i < len(my_list):
        el = my_list[i]
        my_list[i] = my_list[i+1]
        my_list[i+1] = el
        i += 2
else:
    i = 0
    while i < len(my_list) - 1:
        el = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = el
        i += 2
print(my_list)

'''
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''

seasons = int(input("Ведите месяц в виде целого числа от 1 до 12: "))
if seasons <= 12 and seasons >= 1:
    month_dict = {
    1: 'January', 2: 'February',3: 'March',
    4: 'April', 5: 'May', 6: 'June',
    7: 'Jule', 8: 'August', 9: 'September',
    10: 'October', 11: 'November', 12: 'December'
    }
    month_list = list(month_dict.values())
    for i, el in enumerate(month_list):
        if i == seasons-1:
            print(f"Месяц из list {month_list[i]}")
            break
    print(f"Месяц из dict {month_dict[seasons]}")
else:
    print("Время года - ")

'''
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. 
Вывести каждое слово с новой строки. 
Строки необходимо пронумеровать. 
Если в слово длинное, выводить только первые 10 букв в слове.
'''
my_str = input("Ведите строку: ")
a = my_str.split(' ')
for i, el in enumerate(a, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}. - {el}")

'''
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. 
У пользователя необходимо запрашивать новый элемент рейтинга. 
Если в рейтинге существуют элементы с одинаковыми значениями, 
то новый элемент с тем же значением должен разместиться после них.
'''

number = int(input('Введите число: '))
my_list = [7, 4, 3, 2]
c = my_list.count(number)
for element in my_list:
    if c > 0:
        i = my_list.index(number)
        my_list.insert(i+c, number)
        break
    else:
        if number > element:
            j = my_list.index(element)
            my_list.insert(j, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print(my_list)

'''
6. * Реализовать структуру данных «Товары». 
Она должна представлять собой список кортежей. 
Каждый кортеж хранит информацию об отдельном товаре. 
В кортеже должно быть два элемента — 
номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). 
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
'''

goods = []
features = {'название ': '', 'цена ': '', 'количество ': '', 'ед. ': ''}
analytics = {'название ': [], 'цена ': [], 'количество ': [], 'ед. ': []}
num = 0
feature_ = None
control = None
while True:
    control = input("Для выхода нажмите 'Q', для продолжения нажмите 'Enter', для аналитики нажмите 'A'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(f'\n Текущая аналитики \n {"-" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
    for f in features.keys():
        feature_ = input(f'Функция ввода "{f}"')
        features[f] = int(feature_) if (f == 'цена' or f == 'количество') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))

goods = int(input("Введите количество товара "))
n = 1
my_dict = []
my_list = []
my_analys = {}
while n <= goods:
    my_dict = dict({'название ': input("введите название "), 'цена ': input("Введите цену "),
                    'количество ': input('Введите количество '), 'eд ': input("Введите единицу измерения ")})
    my_list.append((n, my_dict))
    n += 1
    my_analys = dict(
        {'название ': my_dict.get('название '), 'цена ': my_dict.get('цена '), 'количество ': my_dict.get('количество '),
         'ед ': my_dict.get('ед ')})
print(my_list)
print(my_analys)



