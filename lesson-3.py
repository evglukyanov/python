'''
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''

def numbers_func(*args):
    try:
        x = int(input("Enter x = "))
        y = int(input("Enter y = "))
        return x / y
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Wrong devider! You can't use zero as a devider"
print(numbers_func())

'''
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: 
имя, фамилия, год рождения, город проживания, email, телефон. 
Функция должна принимать параметры как именованные аргументы. 
Реализовать вывод данных о пользователе одной строкой.
'''

def my_name (name, surname, year, city, email, telephone):
    return ', '.join([name, surname, year, city, email, telephone])
print(my_name(name = 'Evgenii', surname = 'Lukyanov', year = '1978 y/b', city = 'Moskow', email = 'email@mail.ru', telephone = '8-999-1111111'))

'''
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, 
и возвращает сумму наибольших двух аргументов.
'''

def my_func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3
print(f'result = {my_func(int(input("enter first argument: ")), int(input("enter second argument: ")), int(input("enter third argument: ")))}')


'''
4. Программа принимает действительное положительное число x и целое отрицательное число y. 
Необходимо выполнить возведение числа x в степень y. 
Задание необходимо реализовать в виде функции my_func(x, y). 
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. 
Первый — возведение в степень с помощью оператора **. 
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
'''
def my_square(x, y):
    return x ** y
print(f'Rezult = {my_square(5, -2)}')


''''
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. 
При нажатии Enter должна выводиться сумма чисел. 
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. 
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. 
Но если вместо числа вводится специальный символ, выполнение программы завершается. 
Если специальный символ введен после нескольких чисел, 
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
'''

def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введите строку чисел, разделенных пробелом или Q для выхода - ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Текущая сумма {sum_res}')
    print(f'Окончательная сумма {sum_res}')
my_sum()