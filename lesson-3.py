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
