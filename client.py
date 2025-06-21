import socket

if __name__ == "__main__":
   host = '127.0.0.1'
   port = 12345
   totalClients = int(input('Enter number of Client: '))

   s = socket.socket(socket.AF_INET, socket.SOCK_STREAMS) # TCP/IP 
   s.bind((host,port))
   s.listen(totalClients)

   connections = []
   print("Initiating Clinets")

   while True:
      for i in range (totalClients):
         conn = s.accept()
         connections.append(conn)
         print("Connected with client", i+1)