from guess import guess_number, get_data
if __name__ == '__main__':
    min_num, max_num, attempts = get_data()
    print(f'result: {guess_number(min_num, max_num, attempts)}')
