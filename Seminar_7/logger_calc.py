

def log_data(data):
    with open('logger.csv', 'a') as file:
        file.write('{}\n'.format(data))

