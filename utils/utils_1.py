import json
from utils import oper


def get_data():
    """
    :return: переменная с данными по операциям
    """
    with open('operations.txt', 'rt', encoding='utf-8') as file:
        operation_json = file.read()
        operation = json.loads(operation_json)
        return operation


# print(type(get_data()))
# print(get_data())
# print(len(get_data()))


# operation = get_data()
def get_data_executed(operation):
    """
    :param operation: Список данных общий
    :return: Список данные с успешными операциями
    """
    operation_executed = []
    for i in operation:
        if i['state'] == 'EXECUTED':
            operation_executed.append(i)
    return operation_executed
