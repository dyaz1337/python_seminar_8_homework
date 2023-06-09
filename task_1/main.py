"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""

import csv
import os
import re


def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = []

    columns = ['Изготовитель системы', 'Название ОС', 'Код продукта',
               'Тип системы']
    main_data.append(columns)

    for file_num in range(1, 4):
        filename = f'info_{file_num}.txt'
        if not os.path.exists(filename):
            print(f'Файл {filename} не найден')
            continue

        with open(filename) as file:
            data = file.read()

            os_prod_match = re.search(r'Изготовитель системы:\s*([^\n]*)',
                                      data)
            os_name_match = re.search(r'Название ОС:\s*([^\n]*)', data)
            os_code_match = re.search(r'Код продукта:\s*([^\n]*)', data)
            os_type_match = re.search(r'Тип системы:\s*([^\n]*)', data)

            os_prod_list.append(os_prod_match.group(1).strip())
            os_name_list.append(os_name_match.group(1).strip())
            os_code_list.append(os_code_match.group(1).strip())
            os_type_list.append(os_type_match.group(1).strip())

        for i in range(len(os_prod_list)):
            row = [os_prod_list[i], os_name_list[i], os_code_list[i],
                   os_type_list[i]]
            main_data.append(row)

    return main_data


def write_to_csv(filename):
    data = get_data()

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f'Данные записаны в файл {filename}')


write_to_csv('report.csv')
