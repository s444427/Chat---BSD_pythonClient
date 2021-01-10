from Connection import Connection
from Data import Data

if __name__ == '__main__':

    # Set connection with server
    server = Connection()
    server.connect()

    # Prepare to exchange data
    data = Data()

    # Exchange data
    message = data.send(server.client_socket)
    data.receive(server.client_socket)

    while message != 'exit':
        message = data.send(server.client_socket)
        data.receive(server.client_socket)

    # Disconnect
    server.disconnect()
