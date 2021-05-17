import socket
import threading
from postgres_connection import *

HOST = '127.0.0.1'
PORT = 9999

MAX_THREAD = 5
connecting_threads = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

#server side check login
def login(connection):
    connection.send(b'Username: ')
    userName = connection.recv(1024).decode()

    print(userName)

    connection.send(b'Password: ')
    pass_ = connection.recv(1024).decode()
    print(pass_)

    if (db_connection(userName, pass_) == True):
        connection.send(b'Logged in')
    else:
        connection.send(b'Wrong username or password')
    # connecting_threads -= 1

#server side check registration
def registration(connection):
    connection.send(b'Input new username: ')
    userName = connection.recv(1024).decode()
    print(userName)
    connection.send(b'Input password: ')
    pass_ = connection.recv(1024).decode()
    print(pass_)
    # connection.send(b'Re-enter password: ')
    # pass_2 = connection.recv(1024).decode()
    # if (pass_ != pass_2):
    #     connection.send(b'Password are not the same')
    if (db_search_username(userName) == True):
        connection.send(b'Failed to create new account')
    else:
        db_registration(userName, pass_)
        connection.send(b'Create new account success')
    # connecting_threads -= 1


def handle_client(conn, addr):
    print(f'Received connection from {addr}...')

    # login(conn)

    registration(conn)
    close_conn(conn)


def close_conn(connection):
    connection.close()


while True:
    s.listen(MAX_THREAD)
    print('Server is listening...\n')
    conn, addr = s.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.setDaemon(True)
    thread.start()