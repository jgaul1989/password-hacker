import socket
import argparse


BUFFER_SIZE = 1024


def create_socket():
    return socket.socket()

def send_message(client_socket, address, message):
    client_socket.connect(address)
    client_socket.send(message.encode())
    return client_socket.recv(BUFFER_SIZE).decode()


def main(ip_address, port, message):
    address = (ip_address, port)
    with create_socket() as client_socket:
        response = send_message(client_socket, address, message)
        print(response)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("ip_address", type=str)
    parser.add_argument("port", type=int)
    parser.add_argument("message", type=str)
    args = parser.parse_args()

    # Basic validation can be added here
    main(args.ip_address, args.port, args.message)