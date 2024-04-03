import socket
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ip_address", type=str)
    parser.add_argument("port", type=int)
    parser.add_argument("message", type=str)
    args = parser.parse_args()

    with socket.socket() as client_socket:
        host_name = args.ip_address
        port = args.port
        address = (host_name, port)
        client_socket.connect(address)
        data = args.message.encode()
        client_socket.send(data)
        response = client_socket.recv(1024)
        response_str = response.decode()
        print(response_str)