# Программа, которая будет складывать, вычитать, умножать или делить два числа.

import operator

a = 0
b = 1
z = ' '

list_operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv}


def calculator(a, b, z):
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))

    if b == 0:
        print('Ошибка ввода, нельзя делить на 0 ')
        b = int(input('Введите второе число: '))

    z = input('Введите знак сложения +, умножения *, деления /, вычитания - или 0 для завершения работы: ')

    while z != '0' and z not in list_operators:
        print('Ошибка ввода')
        z = input('Введите знак сложения +, умножения *, деления / или вычитания - : ')

    if z == '0': # базовое условие
        print('End')
        exit()
    else:
        print(f'Выражение {a} {z} {b} = ', list_operators[z](a, b))
        return (str(calculator(a, b, z))) # вызов функцией самой себя


print(calculator(a, b, z))
exit()