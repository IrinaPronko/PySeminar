# -*- coding: utf-8 -*-
# Каждое из слов «class», «function», «method» записать в байтовом формате
# без преобразования в последовательность кодов
# (не используя!!! методы encode и decode)
# и определить тип, содержимое и длину соответствующих переменных.

for p in [b'class', b'function', b'method']:
    print(f'Тип - {type(p)}. Содержимое - {p}. Длина - {len(p)}.')
exit()