# -*- coding: utf-8 -*-
# Преобразовать слова «разработка», «администрирование», «protocol»,
# «standard» из строкового представления в байтовое и выполнить
# обратное преобразование (используя методы encode и decode).

for s in ['разработка', 'администрирование', 'protocol', 'standard']:
    p = s.encode('utf-8', 'replace')
    q = p.decode('utf-8')
    print(s, p, q)
exit()