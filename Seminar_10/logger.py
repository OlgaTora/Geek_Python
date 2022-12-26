#Для создания самого файла
# with open('logger.txt', 'w') as file:
#     pass

def logger(data):
    with open('logger.txt', 'a') as file:
        file.write('{}\n'.format(data))

