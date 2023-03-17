# Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата

import yaml
from yaml import SafeLoader


def yaml_save_data():
    my_data = {
        'items': ['computer', 'printer', 'keyboard', 'mouse'],
        'items_ptice': {'computer': '200\u20ac-1000\u20ac', 'keyboard': '5\u20ac-50\u20ac',
                        'mouse': '4\u20ac-7\u20ac', 'printer': '100\u20ac-300\u20ac'},
        'items_quantity': 4
    }

    with open('file.yaml', 'w', encoding='utf-8') as yaml_file:
        yaml.dump(my_data, yaml_file, default_flow_style=False, allow_unicode=True)


def read_yaml_file():
    try:
        with open('file.yaml', 'r', encoding='utf-8') as read_file:
            content = yaml.load(read_file, Loader=SafeLoader)
            return content
    except FileNotFoundError:
        print('файла не существует')


yaml_save_data()
print(read_yaml_file())