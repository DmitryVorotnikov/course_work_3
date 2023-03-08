import json
from datetime import datetime


def get_data():
    """
    :return: переменная с данными по операциям
    """
    with open('operations.txt', 'rt', encoding='utf-8') as file:
        operation_json = file.read()
        operation = json.loads(operation_json)
        return operation


def get_data_executed(operation):
    """
    :param operation: Список данных общий
    :return: Список данных с успешными операциями
    """
    operation_executed = []
    for i in operation:
        if i['state'] == 'EXECUTED':
            operation_executed.append(i)
    return operation_executed


def get_data_del_no_from(operation):
    """
    :param operation: Список данных с успешными операциями
    :return: Список данных с ключом 'from'
    """
    operation_del_no_from = []
    for i in operation:
        if 'from' in i:
            operation_del_no_from.append(i)
    return operation_del_no_from


def get_data_last_5(operation):
    """
    :param operation: Список данных с успешными операциями
    :return: Последние 5 успешных операций
    """
    operation = sorted(operation, key=lambda x: x['date'], reverse=True)
    return operation[:5]


def get_formatted(operation):
    """
    :param operation: Список из 5 элементов отсортированных по дате
    :return: Выводит 5 сообщение в необходимом виде
    """
    formatted_operation = []
    for i in operation:
        date = datetime.strptime(i['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = i['description']
        send = i['from'].split()
        send_bill = send.pop(-1)
        send_bill = f"{send_bill[:4]} {send_bill[4:6]}** **** {send_bill[-4:]}"
        send_info = " ".join(send)
        resipient = f"**{i['to'][-4:]}"
        amount = f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}"
        formatted_operation.append(f"{date} {description}\n{send_info} {send_bill} -> Счет {resipient}\n{amount}\n\n")
    return formatted_operation
