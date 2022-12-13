import user_int as ui


def log_data(data):
    with open('logger.csv', 'a') as file:
        file.write(data)

