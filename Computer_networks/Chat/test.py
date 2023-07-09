import socket
import threading
from time import sleep


yandex_socket = socket.socket()
addr = ("87.250.250.242", 443) #ip yandex
yandex_socket.connect(addr)

data_out = b"GET / HTTP/1.1\r\nHost:ya.ru\r\n\r\n"
yandex_socket.send(data_out)

data_in = b""


def recieving():
    global data_in
    while True:
        data_chunk = yandex_socket.recv(1024)
        data_in = data_in + data_chunk


rec_thread = threading.Thread(target=recieving)
rec_thread.start()

sleep(4)

print(data_in)
yandex_socket.close()
