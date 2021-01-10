import socket


class Connection:
    def __init__(self):
        self.host = socket.gethostname()  # as both code is running on same pc
        self.port = 8989  # socket server port number
        self.client_socket = 0

    def connect(self):
        self.client_socket = socket.socket()  # instantiate
        self.client_socket.connect((self.host, self.port))  # connect to the server
        print("Hello World!")

    def disconnect(self):
        self.client_socket.close()  # close the connection
