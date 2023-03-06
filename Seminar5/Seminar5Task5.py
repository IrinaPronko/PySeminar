# Программа вывода на экран кодов и символов таблицы ASCII, начиная с символа №32 и заканчивая №127-м.

def asc_n(n, asc=None):
    if (n-2) % 10 == 0:
        print()
    if n == 128: # базовое условие
        return asc
    if n < 100:
        asc = ' ' + str(n) + ' - ' + chr(n) + '   '
    else:
        asc = str(n) + ' - ' + chr(n) + '   '
    print(f'{asc:9}', end=' ')
    return "{0}{1}".format(asc, asc_n(n + 1))  # вызов функцией самой себя

n = 32
print('                                  Таблица кодов и символов ASCII')
asc = asc_n(n)
exit()