import multiprocessing
import socket
import struct
import threading
from dbteachers import teachers
from dbstudents import students
from groups import groups
from groupstime import groupstime

cores = multiprocessing.cpu_count()
print(cores)

SIZE = 12

class Server(object):
   def __init__(self, ip, port):
       self.ip = ip
       self.port = port
       self.count = 0
       self.running=True
       self.studentdb = students()
       self.teacherdb = teachers()
       self.format = 'utf-8'
       self.dbgroups = groups()
       self.dbgroupstime = groupstime()

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
                   elif arr != None and arr[0] == "Insertlesson" and len(arr) == 7:
                       print("insert lesson")
                       print(arr)
                       arr_teachers = self.teacherdb.get_teacher_by_email_and_password(arr[5], arr[6])
                       teacherid = arr_teachers[0]
                       server_data = self.dbgroups.insert_group(teacherid,arr[1])
                       if server_data != False:
                           # group = self.dbgroups.get_group_id_by_name(arr[1])
                           group = self.dbgroups.get_group_id_by_name_and_teacher(arr[1],teacherid)
                           timeofgroup = self.dbgroupstime.insert_group_time(group,arr[2],arr[3],arr[4])
                           if timeofgroup == "exist":
                               self.send_msg("exist", client_socket)
                           elif timeofgroup:
                               self.send_msg("inserted", client_socket)
                           else:
                               self.send_msg("not inserted", client_socket)


                   elif arr != None and arr[0] == "deletelesson" and len(arr) == 7:
                       print("delete lesson")
                       print(arr)
                       arr_teachers = self.teacherdb.get_teacher_by_email_and_password(arr[5], arr[6])
                       print(arr_teachers)
                       teacherid = arr_teachers[0]
                       is_exist_id = self.dbgroups.check_teacher_for_group(arr[1],teacherid)
                       if is_exist_id == "failed":
                           self.send_msg("Failed to delete record", client_socket)
                       elif is_exist_id:
                           server_data = self.dbgroups.insert_group(teacherid, arr[1])
                           if server_data != False:
                               group = self.dbgroups.get_group_id_by_name(arr[1])
                               timeofgroup = self.dbgroupstime.delete_group_time(group, arr[2], arr[3], arr[4])
                               if timeofgroup == "not found":
                                   self.send_msg("not found", client_socket)
                               elif timeofgroup == "Success":
                                   self.send_msg("Success", client_socket)
                               elif timeofgroup == "Failed to delete record":
                                   self.send_msg("Failed to delete record", client_socket)
                           else:
                               self.send_msg("Failed to delete record", client_socket)
                       elif not is_exist_id:
                           self.send_msg("not allowed", client_socket)




                   elif arr != None and arr[0] == "updatelesson" and len(arr) == 10:
                       print("update lesson")
                       print(arr)
                       arr_teachers = self.teacherdb.get_teacher_by_email_and_password(arr[8], arr[9])
                       print(arr_teachers)
                       teacherid = arr_teachers[0]
                       is_exist_id = self.dbgroups.check_teacher_for_group(arr[1], teacherid)
                       if is_exist_id == "failed":
                           self.send_msg("Failed", client_socket)
                       elif is_exist_id:
                           server_data = self.dbgroups.insert_group(teacherid, arr[1])
                           if server_data != False:
                               group = self.dbgroups.get_group_id_by_name(arr[1])
                               # groupid = group[0]
                               timeofgroup = self.dbgroupstime.update_group_time(group, arr[2], arr[3], arr[4], group,
                                                                                 arr[5], arr[6], arr[7])
                               if timeofgroup == "Record does not exist":
                                   self.send_msg("not exist", client_socket)
                               elif timeofgroup:
                                   self.send_msg("Success", client_socket)
                               elif not timeofgroup:
                                   self.send_msg("Failed", client_socket)
                       elif not is_exist_id:
                           self.send_msg("not allowed", client_socket)


                   # elif arr != None and arr[0] == "Addgroup" and len(arr) == 5:
                   #     print("Add group")
                   #     print(arr)
                   #     str_addgroup = ",".join(arr)
                   #     print(str_addgroup)
                   #     self.send_msg(str_addgroup, client_socket)
                   #
                   # elif arr != None and arr[0] == "Deletegroup" and len(arr) == 5:
                   #     print("Delete group")
                   #     print(arr)
                   #     str_deletegroup = ",".join(arr)
                   #     print(str_deletegroup)
                   #     self.send_msg(str_deletegroup, client_socket)
                   #
                   # elif arr != None and arr[0] == "Updategroup" and len(arr) == 8:
                   #     print("Update group")
                   #     print(arr)
                   #     str_updategroup = ",".join(arr)
                   #     print(str_updategroup)
                   #     self.send_msg(str_updategroup, client_socket)

                   elif arr != None and arr[0] == "kids tennis" and len(arr) == 1:
                       print("kids tennis")
                       print(arr)
                       # groupId = self.dbgroups.get_group_id_by_name(arr[0])
                       # print(groupId)
                       # arrgroupstime = self.dbgroupstime.get_details_by_group_id(groupId)
                       arrgroupstime = self.dbgroupstime.get_details_by_groupname(arr[0])
                       print(arrgroupstime, "server_kids_tennis")
                       if arrgroupstime == "there is no group":
                           print("there is no group","server_kids_tennis")
                           self.send_msg("there is no group", client_socket)
                       elif arrgroupstime == "error":
                           print("error","server_kids_tennis")
                           self.send_msg("error", client_socket)
                       else:
                           print("defult else")
                           print(arrgroupstime)
                           arrgroup = []
                           for el in arrgroupstime:
                               strgroupstime = ",".join(el)
                               arrgroup.append(strgroupstime)
                           print(arrgroup)
                           arrgroup = "*".join(arrgroup)
                           print(arrgroup)
                           self.send_msg(arrgroup, client_socket)

                   elif arr != None and arr[0] == "swimming" and len(arr) == 1:
                       print("swimming")
                       print(arr)
                       groupId = self.dbgroups.get_group_id_by_name(arr[0])
                       print(groupId)
                       arrgroupstime = self.dbgroupstime.get_details_by_group_id(groupId)
                       print(arrgroupstime, "server_swimming")
                       if arrgroupstime == "there is no group":
                           print("there is no group","server_swimming")
                           self.send_msg("there is no group", client_socket)
                       elif arrgroupstime == "error":
                           print("error","server_swimming")
                           self.send_msg("error", client_socket)
                       else:
                           print("defult else")
                           print(arrgroupstime)
                           arrgroup = []
                           for el in arrgroupstime:
                               strgroupstime = ",".join(el)
                               arrgroup.append(strgroupstime)
                           print(arrgroup)
                           arrgroup = "*".join(arrgroup)
                           print(arrgroup)
                           self.send_msg(arrgroup, client_socket)

                   elif arr != None and arr[0] == "yoga" and len(arr) == 1:
                       print("yoga")
                       print(arr)
                       groupId = self.dbgroups.get_group_id_by_name(arr[0])
                       print(groupId)
                       arrgroupstime = self.dbgroupstime.get_details_by_group_id(groupId)
                       print(arrgroupstime, "server_yoga")
                       if arrgroupstime == "there is no group":
                           print("there is no group","server_yoga")
                           self.send_msg("there is no group", client_socket)
                       elif arrgroupstime == "error":
                           print("error","server_yoga")
                           self.send_msg("error", client_socket)
                       else:
                           print("defult else")
                           print(arrgroupstime)
                           arrgroup = []
                           for el in arrgroupstime:
                               strgroupstime = ",".join(el)
                               arrgroup.append(strgroupstime)
                           print(arrgroup)
                           arrgroup = "*".join(arrgroup)
                           print(arrgroup)
                           self.send_msg(arrgroup, client_socket)

                   elif arr != None and arr[0] == "basketball" and len(arr) == 1:
                       print("basketball")
                       print(arr)
                       groupId = self.dbgroups.get_group_id_by_name(arr[0])
                       print(groupId)
                       arrgroupstime = self.dbgroupstime.get_details_by_group_id(groupId)
                       print(arrgroupstime, "server_basketball")
                       if arrgroupstime == "there is no group":
                           print("there is no group","server_basketball")
                           self.send_msg("there is no group", client_socket)
                       elif arrgroupstime == "error":
                           print("error","server_basketball")
                           self.send_msg("error", client_socket)
                       else:
                           print("defult else")
                           print(arrgroupstime)
                           arrgroup = []
                           for el in arrgroupstime:
                               strgroupstime = ",".join(el)
                               arrgroup.append(strgroupstime)
                           print(arrgroup)
                           arrgroup = "*".join(arrgroup)
                           print(arrgroup)
                           self.send_msg(arrgroup, client_socket)

                   elif arr != None and arr[0] == "dance" and len(arr) == 1:
                       print("dance")
                       print(arr)
                       groupId = self.dbgroups.get_group_id_by_name(arr[0])
                       print(groupId)
                       arrgroupstime = self.dbgroupstime.get_details_by_group_id(groupId)
                       print(arrgroupstime, "server_dance")
                       if arrgroupstime == "there is no group":
                           print("there is no group","server_dance")
                           self.send_msg("there is no group", client_socket)
                       elif arrgroupstime == "error":
                           print("error","server_dance")
                           self.send_msg("error", client_socket)
                       else:
                           print("defult else")
                           print(arrgroupstime)
                           arrgroup = []
                           for el in arrgroupstime:
                               strgroupstime = ",".join(el)
                               arrgroup.append(strgroupstime)
                           print(arrgroup)
                           arrgroup = "*".join(arrgroup)
                           print(arrgroup)
                           self.send_msg(arrgroup, client_socket)

                   elif arr != None and arr[0] == "adults tennis" and len(arr) == 1:
                       print("adults tennis")
                       print(arr)
                       groupId = self.dbgroups.get_group_id_by_name(arr[0])
                       print(groupId)
                       arrgroupstime = self.dbgroupstime.get_details_by_group_id(groupId)
                       print(arrgroupstime, "server_adults_tennis")
                       if arrgroupstime == "there is no group":
                           print("there is no group","server_adults_tennis")
                           self.send_msg("there is no group", client_socket)
                       elif arrgroupstime == "error":
                           print("error","server_adults_tennis")
                           self.send_msg("error", client_socket)
                       else:
                           print("defult else")
                           print(arrgroupstime)
                           arrgroup = []
                           for el in arrgroupstime:
                               strgroupstime = ",".join(el)
                               arrgroup.append(strgroupstime)
                           print(arrgroup)
                           arrgroup = "*".join(arrgroup)
                           print(arrgroup)
                           self.send_msg(arrgroup, client_socket)

                   elif arr != None and arr[0] == "ping pong" and len(arr) == 1:
                       print("ping pong")
                       print(arr)
                       groupId = self.dbgroups.get_group_id_by_name(arr[0])
                       print(groupId)
                       arrgroupstime = self.dbgroupstime.get_details_by_group_id(groupId)
                       print(arrgroupstime, "server_ping_pong")
                       if arrgroupstime == "there is no group":
                           print("there is no group","server_ping_pong")
                           self.send_msg("there is no group", client_socket)
                       elif arrgroupstime == "error":
                           print("error","server_ping_pong")
                           self.send_msg("error", client_socket)
                       else:
                           print("defult else")
                           print(arrgroupstime)
                           arrgroup = []
                           for el in arrgroupstime:
                               strgroupstime = ",".join(el)
                               arrgroup.append(strgroupstime)
                           print(arrgroup)
                           arrgroup = "*".join(arrgroup)
                           print(arrgroup)
                           self.send_msg(arrgroup, client_socket)

                   elif arr != None and arr[0] == "fitness" and len(arr) == 1:
                       print("fitness")
                       print(arr)
                       groupId = self.dbgroups.get_group_id_by_name(arr[0])
                       print(groupId)
                       arrgroupstime = self.dbgroupstime.get_details_by_group_id(groupId)
                       print(arrgroupstime, "server_fitness")
                       if arrgroupstime == "there is no group":
                           print("there is no group","server_fitness")
                           self.send_msg("there is no group", client_socket)
                       elif arrgroupstime == "error":
                           print("error","server_fitness")
                           self.send_msg("error", client_socket)
                       else:
                           print("defult else")
                           print(arrgroupstime)
                           arrgroup = []
                           for el in arrgroupstime:
                               strgroupstime = ",".join(el)
                               arrgroup.append(strgroupstime)
                           print(arrgroup)
                           arrgroup = "*".join(arrgroup)
                           print(arrgroup)
                           self.send_msg(arrgroup, client_socket)

                   elif arr != None and arr[0] == "pilates" and len(arr) == 1:
                       print("pilates")
                       print(arr)
                       groupId = self.dbgroups.get_group_id_by_name(arr[0])
                       print(groupId)
                       arrgroupstime = self.dbgroupstime.get_details_by_group_id(groupId)
                       print(arrgroupstime, "server_pilates")
                       if arrgroupstime == "there is no group":
                           print("there is no group","server_pilates")
                           self.send_msg("there is no group", client_socket)
                       elif arrgroupstime == "error":
                           print("error","server_pilates")
                           self.send_msg("error", client_socket)
                       else:
                           print("defult else")
                           print(arrgroupstime)
                           arrgroup = []
                           for el in arrgroupstime:
                               strgroupstime = ",".join(el)
                               arrgroup.append(strgroupstime)
                           print(arrgroup)
                           arrgroup = "*".join(arrgroup)
                           print(arrgroup)
                           self.send_msg(arrgroup, client_socket)

                   elif arr != None and arr[0] == "boxing" and len(arr) == 1:
                       print("boxing")
                       print(arr)
                       groupId = self.dbgroups.get_group_id_by_name(arr[0])
                       print(groupId)
                       arrgroupstime = self.dbgroupstime.get_details_by_group_id(groupId)
                       print(arrgroupstime, "server_boxing")
                       if arrgroupstime == "there is no group":
                           print("there is no group","server_boxing")
                           self.send_msg("there is no group", client_socket)
                       elif arrgroupstime == "error":
                           print("error","server_boxing")
                           self.send_msg("error", client_socket)
                       else:
                           print("defult else")
                           print(arrgroupstime)
                           arrgroup = []
                           for el in arrgroupstime:
                               strgroupstime = ",".join(el)
                               arrgroup.append(strgroupstime)
                           print(arrgroup)
                           arrgroup = "*".join(arrgroup)
                           print(arrgroup)
                           self.send_msg(arrgroup, client_socket)



                   # elif arr != None and arr[0] == "payment_box" and len(arr) == 2:
                   #     print("payment_box")
                   #     print(arr)




                   else:
                       server_data = "False"
               except:
                   print("error on server error except")
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
   # Sender
   # def send_msg(self, data, client_socket):
   #     try:
   #         print("the message is: " + str(data))
   #         if type(data) != bytes:
   #             data = data.encode()
   #         length = len(data)
   #         length = struct.pack("!I", length)
   #         msg = length + data
   #         print("message with length is " + str(msg))
   #         client_socket.sendall(msg)
   #     except Exception as e:
   #         print("Error with sending message:", e)
   #
   # # Receiver
   # def recv_msg(self, client_socket, ret_type="string"):
   #     try:
   #         length = client_socket.recv(4)
   #         if not length:
   #             print("no length!")
   #             return None
   #         length, = struct.unpack("!I", length)
   #         print("The length is " + str(length))
   #         data = client_socket.recv(length)
   #         if not data:
   #             print("no data!")
   #             return None
   #         print("the data is: " + str(data))
   #         if ret_type == "string":
   #             data = data.decode(self.format)
   #         print(data)
   #         return data
   #     except:
   #         print("error with receiving msg")


if __name__ == '__main__':
   ip = '127.0.0.1'
   port = 1817
   s = Server(ip, port)
   s.start()
