class Data:
    def __init__(self):
        self.data = 0
        self.message = 0

    def send(self, socket):
        self.message = input(" -> ")  # take input

        socket.send(self.message.encode())  # send message
        print("sent")

    def receive(self, socket):
        self.data = socket.recv(1024).decode()  # receive response

        print('Received from server: ' + self.data)  # show in terminal
        print("received")
        return 0
