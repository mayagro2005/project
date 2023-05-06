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
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO {} ({}, {}, {}, {}, {}, {}) VALUES (?, ?, ?, ?, ?, ?)".format(
                self.__tablename, self.__to_username, self.__to_teacher_or_student, self.__from_username,
                self.__from_teacher_or_student, self.__to_usernameId, self.__from_usernameId, self.__message),
                (to_username, to_teacher_or_student, from_username, from_teacher_or_student, to_usernameId,
                 from_usernameId, message))
            conn.commit()
            conn.close()
            print("Message inserted successfully")
            return True
        except:
            print("Error inserting message")
            return False

    def delete_message(self, to_username, to_teacher_or_student, from_username, from_teacher_or_student, to_usernameId,
                       from_usernameId):
        try:
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM {} WHERE {} = ? AND {} = ? AND {} = ? AND {} = ? AND {} = ? AND {} = ?".format(
                self.__tablename, self.__to_username, self.__to_teacher_or_student, self.__from_username,
                self.__from_teacher_or_student, self.__to_usernameId, self.__from_usernameId),
                (to_username, to_teacher_or_student, from_username, from_teacher_or_student, to_usernameId,
                 from_usernameId))
            conn.commit()
            conn.close()
            print("Message deleted successfully")
            return True
        except:
            print("Error deleting message")
            return False

    def __str__(self):
        return "table  name is ", self.__tablename