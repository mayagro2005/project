import multiprocessing
import socket
import threading
from dbteachers import teachers
from dbstudents import students

cores = multiprocessing.cpu_count()
print(cores)

class Server(object):
   def __init__(self, ip, port):
       self.ip = ip
       self.port = port
       self.count = 0
       self.running=True
       self.studentdb = students()
       self.teacherdb = teachers()

   def start(self):
       try:
           print('server starting up on ip %s port %s' % (self.ip, self.port))
           # Create a TCP/IP socket
           self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           self.sock.bind((self.ip, self.port))
           self.sock.listen(3)

           while True:
               print('waiting for a new client')
               clientSocket, client_addresses = self.sock.accept()
               print('new client entered')
               clientSocket.send('Hello this is server'.encode())
               self.count += 1
               print(self.count)
               # implement here your main logic
               self.handleClient(clientSocket, self.count)

       except socket.error as e:
           print(e)

   def handleClient(self, clientSock, current):
       client_handler = threading.Thread(target=self.handle_client_connection, args=(clientSock, current,))
       client_handler.start()

   def handle_client_connection(self, client_socket, current):
       not_crash = True
       print(not_crash)
       while self.running:

           while not_crash:
               try:
                   server_data = client_socket.recv(1024).decode('utf-8')
                   #insert,email,password,firstname
                   arr = server_data.split(",")
                   print(server_data)
                   if arr!=None and arr[0]=="SignUp" and arr[1] == "teacher" and len(arr)==6:
                       print("sign up teacher")
                       print(arr)
                       server_data=self.teacherdb.insert_teacher(arr[2], arr[3], arr[4], arr[5])
                       print("sertver data:",server_data)
                       if server_data:
                           client_socket.send("success register".encode())
                       elif server_data:
                           client_socket.send("failed register".encode())

                   elif arr!=None and arr[0]=="SignUp" and arr[1] == "student" and len(arr)==7:
                       print("sign up student")
                       print(arr)
                       server_data = self.studentdb.insert_student(arr[2], arr[3], arr[4], arr[5], arr[6])
                       print("sertver data:", server_data)
                       if server_data:
                           client_socket.send("success register".encode())
                       elif server_data:
                           client_socket.send("failed register".encode())


                   # elif arr!=None and arr[0] == "get_all_users" and len(arr)==1:
                   #     print("get_all_users")
                   #     server_data=self.userDb.select_all_users()
                   #     server_data = ",".join(server_data) # convert data to string
                   else:
                       server_data ="False"
               except:
                   print("error")
                   not_crash = False
                   break

if __name__ == '__main__':
   ip = '127.0.0.1'
   port = 1803
   s = Server(ip, port)
   s.start()
