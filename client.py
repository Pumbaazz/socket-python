import socket

HOST = '127.0.0.1'
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
msg = s.recv(1024).decode()
print(msg)


def login_client():
    username = input()
    s.sendall(username.encode())
    msg = s.recv(1024).decode()
    print(msg)

    password = input()
    s.sendall(password.encode())
    res = s.recv(1024).decode()
    print(res)

def create_new_account():
    username = input()
    s.sendall(username.encode())
    msg = s.recv(1024).decode()
    print(msg)

    password = input()
    s.sendall(password.encode())
    res = s.recv(1024).decode()
    print(res)

def main():
    # login_client()
    # create_new_account()


if __name__ == '__main__':
    main()
