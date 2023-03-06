# Программа, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
def recAonB(a, b):
    if b == 0:
        return 1
    return a * recAonB(a, b - 1)


a = int(input('Введите число A - '))
b = int(input('Введите число B - '))
res = recAonB(a, b)
print(f'Число {a} в степени {b} равно - {res}')
exit()