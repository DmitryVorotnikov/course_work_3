from utils import code
from utils import utils_1


def test_utils_1_get_data():
    assert type(utils_1.get_data()) != None
    assert type(utils_1.get_data()) == list


def test_utils_1_get_data_exucuted():
    data = [{'state': 'CANCELED'}, {'state': 'EXECUTED'}]
    assert utils_1.get_data_executed(data) == [data[1]]


def test_utils_1_get_data_del_no_from():
    data = ['123', 'from 123', 'from 123']
    assert utils_1.get_data_del_no_from(data) == data[1:]


def test_utils_1_get_data_last_5():
    data = [{'date': '2016-08-26T10:50:58.294041', 'from': '123'},
            {'date': '2015-08-26T10:50:58.294041', 'from': '123'},
            {'date': '2014-08-26T10:50:58.294041', 'from': '123'},
            {'date': '2013-08-26T10:50:58.294041', 'from': '123'},
            {'date': '2012-08-26T10:50:58.294041', 'from': '123'},
            {'date': '2011-08-26T10:50:58.294041', 'from': '123'},
            {'date': '2010-08-26T10:50:58.294041', 'from': '123'},
            {'date': '2009-08-26T10:50:58.294041', 'from': '123'}]
    assert utils_1.get_data_last_5(data) == data[:5]


def test_utils_1_get_formatted():
    data = [{"id": 710136990, "state": "CANCELED", "date": "2018-08-17T03:57:28.607101",
             "operationAmount": {"amount": "66906.45", "currency": {"name": "USD", "code": "USD"}},
             "description": "Перевод организации", "from": "Maestro 1913883747791351",
             "to": "Счет 11492155674319392427"}]
    assert len(utils_1.get_formatted(data)) > 0
