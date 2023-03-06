# Программа вывода числа, обратного по порядку входящих в него цифр введенного числа

def recur_reverse(n):
    global revr_num
    if n > 0: # базовое условие
        reminder = n % 10
        revr_num = (revr_num * 10) + reminder
        recur_reverse(n // 10) # вызов функцией самой себя
    return revr_num

n = int(input("Введите любое натуральное число - "))
revr_num = 0
revr_num = recur_reverse(n)
print(f' Обратное число - ', revr_num)
exit()