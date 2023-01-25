import multiprocessing
import socket
import threading
from dbteachers import teachers
from dbstudents import students

cores = multiprocessing.cpu_count()
print(cores)

SIZE = 8

class Server(object):
   def __init__(self, ip, port):
       self.ip = ip
       self.port = port
       self.count = 0
       self.running=True
       self.studentdb = students()
       self.teacherdb = teachers()
       self.format = 'utf-8'

   def start(self):
       try:
           print('server starting up on ip %s port %s' % (self.ip, self.port))
           # Create a TCP/IP socket
           self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           self.sock.bind((self.ip, self.port))
           # self.sock.listen(3)
           self.sock.listen(0)#This will allow the server to listen to an unlimited or a large number of clients at the same time.

           while True:
               print('waiting for a new client')
               clientSocket, client_addresses = self.sock.accept()
               print('new client entered')
               self.send_msg('Hello this is server', clientSocket)
               self.count += 1
               print(self.count)
               # implement here your main logic
               self.handleClient(clientSocket, self.count)

       except socket.error as e:
           print(e)

   def handleClient(self, clientSock, current):
       client_handler = threading.Thread(target=self.handle_client_connection, args=(clientSock, current,))
       client_handler.daemon= True
       client_handler.start()

   def handle_client_connection(self, client_socket, current):
       not_crash = True
       print(not_crash)
       while self.running:
           while not_crash:
               try:
                   # server_data = client_socket.recv(1024).decode('utf-8')
                   server_data = self.recv_msg(client_socket)
                   #insert,email,password,firstname
                   arr = server_data.split(",")
                   print(server_data)
                   if arr!=None and arr[0]=="SignUp" and arr[1] == "teacher" and len(arr)==6:
                       print("sign up teacher")
                       print(arr)
                       server_data=self.teacherdb.insert_teacher(arr[2], arr[3], arr[4], arr[5])
                       print("sertver data:",server_data)
                       if server_data == "exist":
                           self.send_msg("exist", client_socket)
                           # client_socket.send("exist".encode())
                       elif server_data:
                           self.send_msg("success register",client_socket)
                           # client_socket.send("success register".encode())
                       elif not server_data:
                           self.send_msg("failed register", client_socket)
                           # client_socket.send("failed register".encode())


                   elif arr != None and arr[0] == "SignUp" and arr[1] == "student" and len(arr) == 7:
                       print("sign up student")
                       print(arr)
                       server_data = self.studentdb.insert_student(arr[2], arr[3], arr[4], arr[5], arr[6])
                       print("sertver data:", server_data)
                       if server_data == "exist":
                           self.send_msg("exist", client_socket)
                           # client_socket.send("exist".encode())
                       elif server_data:
                           self.send_msg("success register", client_socket)
                           # client_socket.send("success register".encode())
                       elif not server_data:
                           self.send_msg("failed register", client_socket)
                           # client_socket.send("failed register".encode())



                   elif arr != None and arr[0] == "SignIn" and arr[1] == "teacher" and len(arr) == 6:
                       print("sign in teacher")
                       print(arr)
                       server_data = self.teacherdb.insert_teacher(arr[2], arr[3], arr[4], arr[5])
                       print("sertver data:", server_data)
                       if server_data == "exist":
                           self.send_msg("exist", client_socket)
                           # client_socket.send("exist".encode())
                       elif server_data:
                           self.send_msg("not exist", client_socket)
                           # client_socket.send("not exist".encode())

                   elif arr != None and arr[0] == "SignIn" and arr[1] == "student" and len(arr) == 7:
                       print("sign in student")
                       print(arr)
                       server_data = self.studentdb.insert_student(arr[2], arr[3], arr[4], arr[5], arr[6])
                       print("sertver data:", server_data)
                       if server_data == "exist":
                           self.send_msg("exist", client_socket)
                           # client_socket.send("exist".encode())
                       elif server_data:
                           self.send_msg("not exist", client_socket)
                           # client_socket.send("not exist".encode())

                   elif arr != None and arr[0] == "Send" and arr[1] == "Message":
                       print("message excepted")
                       print(arr)
                       print("sertver data:", server_data)
                       if server_data != " ":
                           self.send_msg("glad you wrote a message", client_socket)
                           # client_socket.send("glad you wrote a message".encode())
                       else:
                           self.send_msg("you can write messages", client_socket)
                           # client_socket.send("you can write messages".encode())
                   # elif arr!=None and arr[0] == "get_all_users" and len(arr)==1:
                   #     print("get_all_users")
                   #     server_data=self.userDb.select_all_users()
                   #     server_data = ",".join(server_data) # convert data to string
                   else:
                       server_data = "False"
               except:
                   print("error")
                   not_crash = False
                   break

   def send_msg(self, data, client_socket):
       try:
           print("the message is: " + str(data))
           length = str(len(data)).zfill(SIZE)
           length = length.encode(self.format)
           print(length)
           if type(data) != bytes:
               data = data.encode()
           print(data)
           msg = length + data
           print("message with length is " + str(msg))
           client_socket.send(msg)
       except:
           print("error with sending msg")

   def recv_msg(self, client_socket, ret_type="string"):
       try:
           length = client_socket.recv(SIZE).decode(self.format)
           if not length:
               print("no length!")
               return None
           print("the length is " + length)
           data = client_socket.recv(int(length))
           if not data:
               print("no data!")
               return None
           print("the data is: " + str(data))
           if ret_type == "string":
               data = data.decode(self.format)
           print(data)
           return data
       except:
           print("error with receiving msg")


if __name__ == '__main__':
   ip = '127.0.0.1'
   port = 1803
   s = Server(ip, port)
   s.start()
