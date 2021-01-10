class Data:
    def __init__(self):
        self.data = ''
        self.message = ''

    def send(self, socket):
        # take input
        self.message = input(" -> ")

        # send message
        socket.send(self.message.encode())
        print("sent")

        # check if exit
        return self.message

    def receive(self, socket):
        # receive response
        self.data = socket.recv(1024).decode()

        # show in terminal
        print('Received from server: ' + self.data)
