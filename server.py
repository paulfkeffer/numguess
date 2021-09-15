import sys, socket, threading, random

HOST = '127.0.0.1'
if len(sys.argv) < 2:
 PORT = 4000
else:
 PORT = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(4)
clients = [] #list of clients connected
lock = threading.Lock()


class chatServer(threading.Thread):
    def __init__(self, (socket,address)):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address= address

    def run(self):
        lock.acquire()
        clients.append(self)
        lock.release()
        print '%s:%s connected.' % self.address
        while True:
            number = random.randint(1, 100)
            for c in clients:
                c.socket.send("+ Hi I'm thinking of a number between 1 and 100, can you guess it?")
            guessed = False
            while guessed == False:
                data = self.socket.recv(1024)
                if not data:
                    break
                for c in clients:
                    try:
                        data = int(data)
                        if int(data) > number:
                            c.socket.send("< Lower")
                        elif int(data) < number:
                            c.socket.send("> higher")
                        else:
                            c.socket.send("* You guessed it! Good Job. Bye.")
                            guessed = True
                            self.socket.close()
                            break
                    except ValueError:
                        c.socket.send("! That was an invalid input, please only enter numbers between 1 and 100")
            break
        print '%s:%s disconnected.' % self.address
        lock.acquire()
        clients.remove(self)
        lock.release()

while True: # wait for socket to connect
    # send socket to chatserver and start monitoring
    chatServer(s.accept()).start()
