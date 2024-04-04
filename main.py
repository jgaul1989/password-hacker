import socket
import argparse
import string
import itertools


BUFFER_SIZE = 1024


def create_socket():
    return socket.socket()


def connect_to_server(client_socket, address):
    client_socket.connect(address)


def send_message(client_socket, message):
    client_socket.send(message.encode())
    return client_socket.recv(BUFFER_SIZE).decode('utf-8')


def generate_password():
    valid_chars = string.ascii_lowercase + string.digits
    for r in range(1, len(valid_chars) + 1):
        for password in itertools.product(valid_chars, repeat=r):
            yield ''.join(password)


def improved_generate_password():
    password_dictionary = read_passwords_from_file()
    for password in password_dictionary:
        for combination in itertools.product(*zip(password.upper(), password.lower())):
            yield "".join(combination)


def read_passwords_from_file():
    with open('passwords.txt', 'r') as file:
        return [line.strip() for line in file]


def main(ip_address, port):
    address = (ip_address, port)
    with create_socket() as client_socket:
        connect_to_server(client_socket, address)
        password_generator = improved_generate_password()
        password = next(password_generator)
        response = send_message(client_socket, password)

        while response != "Connection success!":
            password = next(password_generator)
            response = send_message(client_socket, password)

        print(password)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ip_address", type=str)
    parser.add_argument("port", type=int)
    args = parser.parse_args()
    main(args.ip_address, args.port)
