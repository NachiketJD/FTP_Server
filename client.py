import socket

if __name__ == "__main__":
   host = '127.0.0.1'
   port = 12345
   totalClients = int(input('Enter number of Client: '))
   s = socket.socket()