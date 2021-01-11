#!/usr/bin/env python

from Connection import Connection
from Data import Data

if __name__ == '__main__':

    message = ''
    # Set connection with server
    server = Connection()
    server.connect()

    # Prepare to exchange data
    data = Data()

    # Exchange data
    data.initialise(server.client_socket)
    message = data.send(server.client_socket)
    data.receive(server.client_socket)

    while message != 'exit':
        message = data.send(server.client_socket)
        data.receive(server.client_socket)

    # Disconnect
    server.disconnect()
