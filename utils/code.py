from import_json import operation

operation_executed = []
def select_executed():
    for i in operation:
        if i['state'] == 'EXECUTED':
            operation_executed.append(i)

select_executed()
print(operation_executed)










# [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
#  'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
#  'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'},
