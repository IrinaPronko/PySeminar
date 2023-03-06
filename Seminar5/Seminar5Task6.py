# Игра "Отгадай число"

import random

randnum = random.randint(0, 100)


def forecaster(randnum, t):
    if t == 0:
        print('Вы проиграли(((((')
        exit()
    answer = int(input('Введите число - '))
    if randnum == answer:
        print(f'Верно! Вы угадали число!')
    elif answer != randnum:
        print(f'Неверно, попробуйте еще раз, у Вас осталось {t - 1} попыток.')
        if answer > randnum:
            print('Ваше число больше задуманного')
        else:
            print('Ваше число меньше задуманного')
        return forecaster(randnum, t - 1)


forecaster(randnum, 10)
exit()