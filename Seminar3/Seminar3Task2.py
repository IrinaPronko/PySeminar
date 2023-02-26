# Программа реализации структуры «Рейтинг», представляющей собой невозрастающий набор натуральных чисел
print('Добрый день!')
lst_rat = [45, 25, 10, 8, 1]
print(f'Текущий рейтинг: {lst_rat}')
new_rat_count = int(input('Сколько вы хотите ввести новых элементов рейтинга - '))
i = 1
while i < new_rat_count + 1:
    new_score = int(input('Введите новый элемент рейтинга: '))
    if new_score > 0:
        lst_rat.append(new_score)
        lst_rat.sort(reverse=True)
        print(f'Новый рейтинг: {lst_rat}')
        i = i + 1
    else:
        print('Ошибка. Вы ввели ненатуральное число')
exit()
