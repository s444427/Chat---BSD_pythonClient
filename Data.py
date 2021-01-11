class Data:
    def __init__(self):
        self.package = ''
        self.message = ''
        self.file = open('receive.txt', 'wb')
        self.counter = 0

    def initialise(self, socket):
        # take input
        self.message = 'csharp'

        # send message
        socket.send(self.message.encode())
        print("Inicialised on python side")

        # check if exit
        return self.message

    def send(self, socket):
        # take input
        self.message = input()
        print(self.message)

        # send message
        socket.send(self.message.encode())
        print("sent")

        # check if exit
        return self.message

    def receive(self, socket):
        print('Waiting for response')
        # receive response
        self.package = socket.recv(4096)

        while self.package:
            print('Receiving')
            self.file.write(self.package)
            print(self.package)
            self.counter = self.counter + 1
            print('Received ' + str(self.counter) + ' package/s')
            self.package = socket.recv(4096)

        self.file.close()
        print('Receiving finished')
