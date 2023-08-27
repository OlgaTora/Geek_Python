import argparse
from logger import logger
from guess import guess_number


def parse():
    parser = argparse.ArgumentParser(prog='guess module',
                                     description='game "guess number"')
    parser.add_argument('-s', '--minimum',
                        help='mininmum bound of guess number',
                        required=True,
                        type=int)
    parser.add_argument('-f',
                        '--maximum', help='maximum bound of guess number',
                        required=True,
                        type=int)
    parser.add_argument('-a', '--attempts',
                        help='attempts for guess',
                        required=True,
                        type=int)
    try:
        arguments = parser.parse_args()
    except SystemExit as e:
        log_msg = 'Quantity of arguments must be 3'
        print(log_msg)
        logger.error(f'{e}: {log_msg}')
    else:
        return guess_number(arguments.minimum, arguments.maximum, arguments.attempts)
