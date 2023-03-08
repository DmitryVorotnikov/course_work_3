from utils import utils_1

def main():
    get_data = utils_1.get_data()
    get_data_executed = utils_1.get_data_executed(get_data)
    get_data_del_no_from = utils_1.get_data_del_no_from(get_data_executed)
    get_data_last_5 = utils_1.get_data_last_5(get_data_del_no_from)
    get_data_formatted = utils_1.get_formatted(get_data_last_5)
    return get_data_formatted

print(main())

