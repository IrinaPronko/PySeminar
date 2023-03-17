# Написать скрипт, автоматизирующий заполнение данными файла в формате JSON с информацией о заказах.
import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json') as f_n:
        dict_to_json = json.load(f_n)
        dict_to_json['orders'].append({
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date,
        })
    with open('orders.json', 'w') as f_w:
        json.dump(dict_to_json, f_w, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    write_order_to_json('Tablet', '1', '700', 'Sidoroff', '22.10.2022')
    write_order_to_json('Smartphone', '2', '1500', 'Smith', '22.11.2022')
