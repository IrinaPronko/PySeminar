# Программа подсчета четных и нечетных цифр введенного натурального числа

def func(num, even=0, odd=0):
    if not num: # базовое условие
        return even, odd
    if num % 10 % 2 == 1:
        odd += 1
    else:
        even += 1
    return func(num // 10, even, odd) # вызов функцией самой себя


n = int(input('Введите любое натуральное число - '))
print(f'Количество четных и нечетных цифр в веденном числе - ', func(n))
exit()
