# Программа поиска в массиве A[1..N] самого близкого по величине элемента к заданному числу X
n = abs(int(input('Введите количество элементов массива А - ')))
a_entered = input('Введите через пробел элементы массива А - ').split()
a_num = list(map(int, a_entered))
if len(a_num) != n:
    print('Введенные элементы не соответствуют заявленному количеству!')
else:
    x = int(input('Введите число X, с которым необходимо сравнивать элементы массива А - ').strip())
    mnm = abs(x - a_num[0])
    res = 0
    for i in range(1, n):
        count = abs(x - a_num[i])
        if count < mnm:
            mnm = count
            res = i
    print(f'Число {a_num[res]} в массиве A наиболее близко по величине к числу {x}, их разница составляет {abs(x - a_num[res])}')
exit()