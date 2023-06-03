import sqlite3
import hashlib

class send_recv_messages(object):
    def __init__(self, tablename = "send_recv_messages",messages_Id = "messages_Id", to_username = "to_username",to_teacher_or_student = "to_teacher_or_student", from_username = "from_username",from_teacher_or_student = "from_teacher_or_student", to_usernameId = "to_usernameId", from_usernameId = "from_usernameId", message = "message"):
        self.__tablename = tablename
        self.__messages_Id = messages_Id
        self.__to_username = to_username
        self.__to_teacher_or_student = to_teacher_or_student
        self.__from_username = from_username
        self.__from_teacher_or_student = from_teacher_or_student
        self.__to_usernameId = to_usernameId
        self.__from_usernameId = from_usernameId
        self.__message = message

        conn = sqlite3.connect('test.db')
        print ("Opened database successfully")
        str = "CREATE TABLE IF NOT EXISTS " + self.__tablename + "(" + self.__messages_Id + " " + "INTEGER PRIMARY KEY AUTOINCREMENT ,"
        str += " " + self.__to_username + " TEXT    NOT NULL ,"
        str += " " + self.__to_teacher_or_student + " TEXT    NOT NULL ,"
        str += " " + self.__from_username + " TEXT    NOT NULL, "
        str += " " + self.__from_teacher_or_student + " TEXT    NOT NULL ,"
        str += " " + self.__to_usernameId + " TEXT    NOT NULL, "
        str += " " + self.__from_usernameId + " TEXT    NOT NULL, "
        str += " " + self.__message + " TEXT    NOT NULL) "
        conn.execute(str)
        print("Table created successfully");
        conn.commit()
        conn.close()
    def get_table_name(self):
        return self.__tablename
    def get_all_messages(self):
        try:
            conn = sqlite3.connect('test.db')
            print("Opened database successfully");
            str1 = "select*from " + self.__tablename
            print(str1)
            cursor = conn.execute(str1)
            rows = cursor.fetchall()
            arr_messages = []
            for row in rows:
                arr_messages.append({
                    "messages_Id": row[0],
                    "to_username": row[1],
                    "to_teacher_or_student": row[1],
                    "from_username": row[2],
                    "from_teacher_or_student": row[1],
                    "to_usernameId": row[3],
                    "from_usernameId": row[4],
                    "message": row[5]
                })
                # str_rows = str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4])
                # arr_teachers.append(str_rows)

            print(arr_messages)
            return arr_messages
        except:
            return False

    def insert_message(self, to_username, to_teacher_or_student, from_username, from_teacher_or_student, to_usernameId,
                       from_usernameId, message):
        try:
            # print(to_username, to_teacher_or_student, from_username, from_teacher_or_student, to_usernameId,
            #       from_usernameId, message)
            # to_username = to_username.replace(" ", "_")
            # from_username = from_username.replace(" ", "_")
            conn = sqlite3.connect('test.db')
            # query = "INSERT INTO {} ({}, {}, {}, {}, {}, {}, {}) VALUES (?, ?, ?, ?, ?, ?, ?)".format(
            #     self.__tablename, self.__to_username, self.__to_teacher_or_student, self.__from_username,
            #     self.__from_teacher_or_student, self.__to_usernameId, self.__from_usernameId, self.__message)
            # print(query)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO {} ({}, {}, {}, {}, {}, {}, {}) VALUES (?, ?, ?, ?, ?, ?, ?)".format(
                self.__tablename, self.__to_username, self.__to_teacher_or_student, self.__from_username,
                self.__from_teacher_or_student, self.__to_usernameId, self.__from_usernameId, self.__message),
                (to_username, to_teacher_or_student, from_username, from_teacher_or_student, to_usernameId,
                 from_usernameId, message))
            conn.commit()
            conn.close()
            print("Message inserted successfully")
            return True
        except Exception as e:
            print("Error inserting message: ", e)
            return False

    def delete_message(self, to_username, to_teacher_or_student, from_username, from_teacher_or_student, to_usernameId,
                       from_usernameId, message):
        try:
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM {} WHERE {} = ? AND {} = ? AND {} = ? AND {} = ? AND {} = ? AND {} = ? AND {} = ?".format(
                    self.__tablename, self.__to_username, self.__to_teacher_or_student, self.__from_username,
                    self.__from_teacher_or_student, self.__to_usernameId, self.__from_usernameId, self.__message),
                (to_username, to_teacher_or_student, from_username, from_teacher_or_student, to_usernameId,
                 from_usernameId, message))
            conn.commit()
            conn.close()
            print("Message deleted successfully")
            return True
        except:
            print("Error deleting message")
            return False

    def get_received_messages(self, to_username, to_teacher_or_student, to_usernameId):
        try:
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            cursor.execute("SELECT {} FROM {} WHERE {} = ? AND {} = ? AND {} = ?".format(
                self.__message, self.__tablename, self.__to_username, self.__to_teacher_or_student,
                self.__to_usernameId),
                (to_username, to_teacher_or_student, to_usernameId))
            messages = [row[0] for row in cursor.fetchall()]
            conn.close()
            print(messages)
            return messages
        except Exception as e:
            print("Error getting messages: ", e)
            return []

    def update_names(self, old_to_username, old_from_username, new_to_username, new_from_username):
        try:
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            cursor.execute(
                f"UPDATE {self.__tablename} SET {self.__to_username} = ?, {self.__from_username} = ? WHERE {self.__to_username} = ? AND {self.__from_username} = ?",
                (new_to_username, new_from_username, old_to_username, old_from_username))
            conn.commit()
            conn.close()
            print("Names updated successfully")
            return True
        except Exception as e:
            print("Error updating names: ", e)
            return False

    # def get_messages_for_recipient(self, to_username, to_teacher_or_student, to_usernameId):
    #     try:
    #         conn = sqlite3.connect('test.db')
    #         cursor = conn.cursor()
    #         query = "SELECT from_username, from_teacher_or_student, message FROM send_recv_messages WHERE to_username=? AND to_teacher_or_student=? AND to_usernameId=?"
    #         cursor.execute(query, (to_username, to_teacher_or_student, to_usernameId))
    #         rows = cursor.fetchall()
    #         messages = []
    #         for row in rows:
    #             messages.append({
    #                 row[0],
    #                 row[1],
    #                 row[2]
    #             })
    #         conn.close()
    #         print(messages)
    #         return messages
    #     except Exception as e:
    #         print("Error retrieving messages: ", e)
    #         return None
    def get_messages_for_recipient(self, to_username, to_teacher_or_student, to_usernameId):
        try:
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            query = "SELECT from_username, from_teacher_or_student, message FROM send_recv_messages WHERE to_username=? AND to_teacher_or_student=? AND to_usernameId=?"
            cursor.execute(query, (to_username, to_teacher_or_student, to_usernameId))
            rows = cursor.fetchall()
            messages = []
            for row in rows:
                messages.append([row[0], row[1], row[2]])
            conn.close()
            print(messages)
            return messages
        except Exception as e:
            print("Error retrieving messages: ", e)
            return None

    def send_recv_messages_to_students(self, to_username, from_username, from_teacher_or_student, from_usernameId,
                                       message):
        try:
            if to_username == "all students":
                conn = sqlite3.connect('test.db')
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM students")
                rows = cursor.fetchall()
                for row in rows:
                    student_username = row[1] + ' ' + row[2]
                    student_Id = row[0]
                    self.insert_message(student_username, "student", from_username, from_teacher_or_student, student_Id,
                                        from_usernameId, message)
                conn.commit()
                conn.close()
                print("message was sent successfully")
                return True
        except:
            print("Error")
            return False

    def send_recv_messages_to_teachers(self, to_username, from_username, from_teacher_or_student, from_usernameId,
                                       message):
        try:
            if to_username == "all teachers":
                conn = sqlite3.connect('test.db')
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM teachers")
                rows = cursor.fetchall()
                for row in rows:
                    teacher_username = row[1] + ' ' + row[2]
                    teacher_Id = row[0]
                    self.insert_message(teacher_username, "teacher", from_username, from_teacher_or_student, teacher_Id,
                                        from_usernameId, message)
                conn.commit()
                conn.close()
                print("message was sent successfully")
                return True
        except:
            print("Error")
            return False

    def __str__(self):
        return "table  name is ", self.__tablename

# s = send_recv_messages()
# s.send_recv_messages_to_students("all students", "lilya qwew", "teacher", 6, "hey everyone")
# s.get_messages_for_recipient("dcf qwey","student","1")
# s.delete_message("dcf qwey","student","lilya qwew","teacher","1","6","hello")
# s.insert_message("dcf qwey","student","lilya qwew","teacher","1","6","hello")
# s.update_names("dcf_qwey","lilya_qwew","dcf qwey","lilya qwew")
# s.get_received_messages("lfgh opyw","student","2")