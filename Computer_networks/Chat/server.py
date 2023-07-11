import socket
import threading

# Connection Data
host = '192.168.0.102'
port = 55555

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Map For Clients and Their Nicknames
clients = {}


# Sending Messages To All Connected Clients
def broadcast(message):
    for client in clients.keys():
        client.send(message)


# Handling Messages From Clients
def handle(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            broadcast(message)
        except (ConnectionError, OSError):
            left_client = clients.get(client)
            clients.pop(client)
            client.close()
            # Removing And Closing Clients
            if len(clients) > 0:
                broadcast(f"{left_client} left!".encode('utf-8'))
            break


# Receiving / Listening Function
def receive():
    while True:
        try:
            # Accept Connection
            client, address = server.accept()
            print(f"Connected with {str(address)}")

            # Request And Store Nickname
            client.send('NICK'.encode('utf-8'))
            nickname = client.recv(1024).decode('utf-8')
            clients[client] = nickname

            # Print And Broadcast Nickname
            print(f"Nickname is {nickname}")
            broadcast(f"{nickname} joined!".encode('utf-8'))
            client.send('Connected to server!'.encode('utf-8'))

            # Start Handling Thread For Client
            thread = threading.Thread(target=handle, args=(client,))
            thread.start()
        except OSError:
            print("You have a problem with connection")

print("Server is listening...")
receive()

