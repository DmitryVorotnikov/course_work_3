import json
# Модуль импортирует данные по операциям и переводит в пайтон словарь.

def open_json():
    """
    :return: переменная с данными по операциям
    """
    with open('operations.py', 'rt', encoding='utf-8') as file:
        operation_json = file.read()
        return operation_json


# В переменную запишем данные по операциям в виде словаря пайтон
operation = json.loads(open_json())
