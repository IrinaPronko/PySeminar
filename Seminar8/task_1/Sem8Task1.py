# Программа работы с csv файлом
import re
import csv


def get_data():
    list_file = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    list_template = [
        r'Изготовитель системы:\s+([a-zA-Z]+)',
        r'Название ОС:\s+([a-zA-Z0-9А-Яа-я\s\.]{1,})[\n]',
        r'Код продукта:\s+([-0-9a-zA-Z]+)',
        r'Тип системы:\s+([-0-9a-zA-Z\s]+)[\n]',
    ]
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    for i in list_file:
        with open(i, encoding='cp1251') as file_in:
            input = file_in.read()
        os_prod_list.append(','.join(re.findall(list_template[0], input)))
        os_name_list.append(','.join(re.findall(list_template[1], input)))
        os_code_list.append(','.join(re.findall(list_template[2], input)))
        os_type_list.append(','.join(re.findall(list_template[3], input)))
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы'], [], [], []]
    for i in range(len(os_name_list)):
        main_data[i + 1].append(os_prod_list[i])
        main_data[i + 1].append(os_name_list[i])
        main_data[i + 1].append(os_code_list[i])
        main_data[i + 1].append(os_type_list[i])
    return main_data


def write_to_csv(file_name):
    with open(file_name, 'w') as f_t:
        wrtie_csv = csv.writer(f_t, delimiter=',')
        data = get_data()
        for i in data:
            wrtie_csv.writerow(i)


write_to_csv('Sem8Task1.csv')
