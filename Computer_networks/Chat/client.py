import socket
import threading


# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except (ConnectionError, OSError):
            # Close Connection When Error
            print("An error occurred!")
            client.close()
            break


def write():
    while True:
        data = input('')
        message = f"{nickname}: {data}"
        if data != 'exit':
            client.send(message.encode('utf-8'))
        else:
            client.close()
            break

try:
    # Choosing Nickname
    nickname = input("Choose your nickname: ")

    # Connecting To Server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('192.168.0.102', 55555))

    # Starting Threads For Listening And Writing
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    write_thread = threading.Thread(target=write)
    write_thread.start()
except OSError:
    print("You dont have connection with server")


