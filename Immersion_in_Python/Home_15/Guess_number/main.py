from parser import parse
from guess import guess_number, get_data
from logger import logger

if __name__ == '__main__':
    parse()

    # def run_game():
    #     try:
    #         min_num, max_num, attempts = get_data()
    #     except ValueError as e:
    #         log_msg = 'Quantity of arguments must be 3'
    #         print(log_msg)
    #         logger.info(f'{e}: {log_msg}')
    #     else:
    #         guess_number(min_num, max_num, attempts)


