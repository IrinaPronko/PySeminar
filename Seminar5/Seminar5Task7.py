# Программа, проверяющая, что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2.

def sum_numbers(n):
    if n == 1:
        return 1
    return n + sum_numbers(n - 1)


n = int(input('Введите любое натуральное число - '))
left = sum_numbers(n)
right = int(n * (n + 1) / 2)
if left == right:
    print(f'{left} = {right}')
    print(f'Для числа {n} равенство выполняется.')
else:
    print(f'{left} <> {right}')
    print(f'Для числа {n} равенство не выполняется.')
exit()