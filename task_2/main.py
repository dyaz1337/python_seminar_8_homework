"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": []
}

вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""

import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', 'r+') as file:
        try:
            orders = json.load(file)
        except:
            orders = {"orders": []}
        order_dict = {"item": item, "quantity": quantity, "price": price,
                      "buyer": buyer, "date": date}
        orders["orders"].append(order_dict)
        file.seek(0)
        json.dump(orders, file, indent=4)


# Пример использования функции
write_order_to_json("printer", "1", "50000", "Ivanov I.I.", "2021-08-01")
write_order_to_json("scanner", "2", "70000", "Petrov P.P.", "2021-08-02")
