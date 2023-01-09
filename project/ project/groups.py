import sqlite3
import hashlib

class groups(object):
    def __init__(self, tablename = "groups", groupId = "groupId", teacherId = "teacherId", nameofgroup = "nameofgroup"):
        self.__tablename = tablename
        self.__groupId = groupId
        self.__teacherId = teacherId
        self.__nameofgroup = nameofgroup


        conn = sqlite3.connect('test.db')
        print ("Opened database successfully")
        str = "CREATE TABLE IF NOT EXISTS " + self.__tablename + "(" + self.__groupId + " " + "INTEGER PRIMARY KEY AUTOINCREMENT ,"
        str += " " + self.__teacherId + " TEXT    NOT NULL ,"
        str += " " + self.__nameofgroup + " TEXT    NOT NULL) "
        conn.execute(str)
        print("Table created successfully");
        conn.commit()
        conn.close()
    def get_table_name(self):
        return self.__tablename
    def get_all_groups(self):
        try:
            conn = sqlite3.connect('test.db')
            print("Opened database successfully");
            str1 = "select*from " + self.__tablename
            print(str1)
            cursor = conn.execute(str1)
            rows = cursor.fetchall()
            arr_groups = []
            for row in rows:
                arr_groups.append({
                    "groupId": row[0],
                    "teacherId": row[1],
                    "nameofgroup": row[2]
                })

                # str_rows = str(row[0]) + " " + str(row[1]) + " " + str(row[2])
                # arr_groups.append(str_rows)
            print(arr_groups)
            return arr_groups
        except:
            return False

    def insert_group(self, teacherId, nameofgroup):
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()

        # Check if the group already exists
        str_check = f"SELECT * from {self.__tablename} where {self.__teacherId} = '{teacherId}' and " \
                    f"{self.__nameofgroup} = '{nameofgroup}'"
        print(str_check)
        cursor.execute(str_check)
        row = cursor.fetchall()
        if row:
            print("Group already exists")
            return False
        else:
            try:
                # Insert the group into the table
                str_insert = f"INSERT INTO {self.__tablename} ({self.__teacherId}, {self.__nameofgroup}) " \
                             f"VALUES ('{teacherId}', '{nameofgroup}')"
                print(str_insert)
                cursor.execute(str_insert)
                conn.commit()
                print("Record created successfully")
                return True
            except:
                print("Failed to insert group")
                return False
            finally:
                conn.close()

    # def insert_group(self, teacherId, nameofgroup):
    #     conn = sqlite3.connect('test.db')
    #     print("Opened database successfully")
    #
    #     str_check = f"SELECT * from {self.__tablename} where {teacherId} = {self.__teacherId} and " \
    #                 f"{nameofgroup} = {self.__nameofgroup}"
    #     print(str_check)
    #     cursor = conn.execute(str_check)
    #     row = cursor.fetchall()
    #     if row:
    #         print("Exist")
    #         return True
    #     else:
    #         try:
    #             # salt = 'GROSSMAN'
    #             # salt_password = hashlib.md5(salt.encode('utf-8') + password.encode('utf-8')).hexdigest()
    #             # print(salt_password)
    #             str_insert = "INSERT INTO " + self.__tablename + " (" + self.__teacherId + "," + self.__nameofgroup + \
    #                          ") VALUES (" + "'" + teacherId + "'" + "," + "'" + nameofgroup + "');"
    #             print(str_insert)
    #             conn.execute(str_insert)
    #             conn.commit()
    #             conn.close()
    #             print("Record created successfully");
    #             return True
    #         except:
    #             print("Failed to insert user")
    #             return False



    def delete_group(self, groupId, teacherId, nameofgroup):
        try:
            conn = sqlite3.connect('test.db')
            str_delete = "DELETE  from " + self.__tablename + " where " + self.__groupId + "=" + "'"+str(groupId)+"'" +\
                         ' and ' + self.__teacherId + "=" + "'"+str(teacherId)+ "'" + ' and ' + self.__nameofgroup + "=" + "'"+str(nameofgroup) + "'"
            print(str_delete)
            conn.execute(str_delete)
            conn.commit()
            conn.close()
            print("Record deleted successfully")
            return "Success"
        except:
            return "Failed to delete user"

    def delete_group_by_Id(self, groupId):
        try:
            conn = sqlite3.connect('test.db')
            str_delete = "DELETE  from " + self.__tablename + " where " + self.__groupId + "=" + "'" + str(
                groupId) + "'"
            print(str_delete)
            conn.execute(str_delete)
            conn.commit()
            conn.close()
            print("Record deleted successfully")
            return "Success"
        except:
            return "Failed to delete user"

    # def is_exist(self, email, password):
    #     conn = sqlite3.connect('test.db')
    #     print("Opened database successfully")
    #     salt = 'GROSSMAN'
    #     salt_password = hashlib.md5(salt.encode('utf-8') + password.encode('utf-8')).hexdigest()
    #
    #     str_check = f"SELECT * from {self.__tablename} where '{email}' = {self.__email} and " \
    #                 f"'{salt_password}' = {self.__password}"
    #     print(str_check)
    #     cursor = conn.execute(str_check)
    #     row = cursor.fetchall()
    #     if row:
    #         print("Exist")
    #         return True
    #     else:
    #         print("Not exist")
    #         return False

    # def update_group_by_Id(self, groupId, teacherId, nameofgroup, groupId1, teacherId1, nameofgroup1):
    #     try:
    #         conn = sqlite3.connect('test.db')
    #         str_update = " UPDATE " + self.__tablename + " set "
    #         str_update += self.__groupId + "=" + "'" + groupId + "',"
    #         str_update += self.__teacherId + "=" + "'" + teacherId + "',"
    #         str_update += self.__nameofgroup + "=" + "'" + nameofgroup + "'"
    #         str_update += " WHERE " + self.__groupId + "=" + "'" + groupId1 + "'"
    #         str_update += " and " + self.__teacherId + "=" + "'" + teacherId1 + "'"
    #         str_update += " and " + self.__nameofgroup + "=" + "'" + nameofgroup1 + "'"
    #
    #         # str_update += " WHERE " + self.__firstname + "=" + "'" + firstname1 + "',"
    #         # str_update += self.__lastname + "=" + "'" + lastname1 + "',"
    #         # str_update += self.__priceforayear + "=" + "'" + priceforayear1 + "',"
    #         # str_update += self.__email + "=" + "'" + email1 + "',"
    #         # str_update += self.__password + "=" + "'" + password1 + "'"
    #         print(str_update)
    #         conn.execute(str_update)
    #         conn.commit()
    #         conn.close()
    #         print("teacher updated successfully")
    #         return "Success"
    #     except:
    #         print("error")
    #         return "Failed to update user by id"


    def update_group(self, teacherId, nameofgroup,  teacherId1, nameofgroup1):
        try:
            conn = sqlite3.connect('test.db')
            str_update = " UPDATE " + self.__tablename + " set "
            str_update += self.__teacherId + "=" + "'" + teacherId + "',"
            str_update += self.__nameofgroup + "=" + "'" + nameofgroup + "'"
            str_update += " WHERE " + self.__teacherId + "=" + "'" + teacherId1 + "'"
            str_update += " and " + self.__nameofgroup + "=" + "'" + nameofgroup1 + "'"

            # str_update += " WHERE " + self.__firstname + "=" + "'" + firstname1 + "',"
            # str_update += self.__lastname + "=" + "'" + lastname1 + "',"
            # str_update += self.__priceforayear + "=" + "'" + priceforayear1 + "',"
            # str_update += self.__email + "=" + "'" + email1 + "',"
            # str_update += self.__password + "=" + "'" + password1 + "'"
            print(str_update)
            conn.execute(str_update)
            conn.commit()
            conn.close()
            print("teacher updated successfully")
            return "Success"
        except:
            print("error")
            return "Failed to update user by id"


    def get_group_by_id(self, groupId):
        try:
            conn = sqlite3.connect('test.db')
            print("Opened database successfully")
            # salt = 'GROSSMAN'
            # salt_password = hashlib.md5(salt.encode('utf-8') + password.encode('utf-8')).hexdigest()
            # print(salt_password)
            # strsql= f"SELECT * from {self.__tablename} where '{self.__email}' = {str(email)} and {self.__password}" \
            #             f" = '{str(salt_password)}"
            # print(strsql)

            strsql = "SELECT * from " + self.__tablename + " where " + self.__groupId + "=" + "'" + str(groupId) + "'"
            print(strsql)
            cursor = conn.execute(strsql)
            row = cursor.fetchone()
            arr_students = []
            if row:
                str_rows = str(row[0]) + " " + str(row[1]) + " " + str(row[2])
                # return [row[0], row[1], row[2], row[3], row[4]]
                arr_students.append(str_rows)
                print(arr_students)
                return arr_students
                # return [row[0], row[1], row[2], row[3], row[4]]

            else:
                print("Failed to find user")
                return False
            conn.commit()
            conn.close()
        except:
            return False

    def get_group_by_teacherId(self, teacherId):
        try:
            conn = sqlite3.connect('test.db')
            print("Opened database successfully")
            # salt = 'GROSSMAN'
            # salt_password = hashlib.md5(salt.encode('utf-8') + password.encode('utf-8')).hexdigest()
            # print(salt_password)
            # strsql= f"SELECT * from {self.__tablename} where '{self.__email}' = {str(email)} and {self.__password}" \
            #             f" = '{str(salt_password)}"
            # print(strsql)

            strsql = "SELECT * from " + self.__tablename + " where " + self.__teacherId + "=" + "'" + str(teacherId) + "'"
            print(strsql)
            cursor = conn.execute(strsql)
            row = cursor.fetchone()
            arr_students = []
            if row:
                str_rows = str(row[0]) + " " + str(row[1]) + " " + str(row[2])
                # return [row[0], row[1], row[2], row[3], row[4]]
                arr_students.append(str_rows)
                print(arr_students)
                return arr_students
                # return [row[0], row[1], row[2], row[3], row[4]]

            else:
                print("Failed to find user")
                return False
            conn.commit()
            conn.close()
        except:
            return False


    def get_student_by_email(self, email):
        try:
            conn = sqlite3.connect('test.db')
            print("Opened database successfully")
            # salt = 'GROSSMAN'
            # salt_password = hashlib.md5(salt.encode('utf-8') + password.encode('utf-8')).hexdigest()
            # print(salt_password)
            # strsql= f"SELECT * from {self.__tablename} where '{self.__email}' = {str(email)} and {self.__password}" \
            #             f" = '{str(salt_password)}"
            # print(strsql)

            strsql = "SELECT * from " + self.__tablename + " where " + self.__email + "=" + "'" + str(email) + "'"
            print(strsql)
            cursor = conn.execute(strsql)
            row = cursor.fetchone()
            arr_students = []
            if row:
                str_rows = str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4])
                # return [row[0], row[1], row[2], row[3], row[4]]
                arr_students.append(str_rows)
                print(arr_students)
                return arr_students

            else:
                print("Failed to find user")
                return False
            conn.commit()
            conn.close()
        except:
            return False


    def get_student_by_email_and_password(self, email, password):
        try:
            conn = sqlite3.connect('test.db')
            print("Opened database successfully")
            # salt = 'GROSSMAN'
            # salt_password = hashlib.md5(salt.encode('utf-8') + password.encode('utf-8')).hexdigest()
            # print(salt_password)
            # strsql= f"SELECT * from {self.__tablename} where '{self.__email}' = {str(email)} and {self.__password}" \
            #             f" = '{str(salt_password)}"
            # print(strsql)

            strsql = "SELECT * from " + self.__tablename + " where " + self.__email + "=" + "'" + str(email) + "'" + ' and ' + self.__password + "=" + "'" + str(password) + "'"
            print(strsql)
            cursor = conn.execute(strsql)
            row = cursor.fetchone()
            arr_students = []
            if row:
                str_rows = str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4])
                # return [row[0], row[1], row[2], row[3], row[4]]
                arr_students.append(str_rows)
                print(arr_students)

                return arr_students

            else:
                print("Failed to find user")
                return False
            conn.commit()
            conn.close()
        except:
            return False

    def __str__(self):
        return "table  name is ", self.__tablename

    def inner(self):
        conn = sqlite3.connect('test.db')
        st = f"select nameofgroup from group inner join teachers on group.teacherId = teachers.teacherId"
        print(st)
        y = conn.execute(st)
        arr = []
        for row in y:
            str1 = row[0] + " " + str(row[1]) + " " + str(row[2])
            arr.append(str1)
        print(arr)

        conn.commit()
        conn.close()
        return arr


g = groups()
# g.insert_group('3',"dance")
# s.insert_student("dcf", "qwey", '250', "mha.com", '9o234')
# s.insert_student("bgka", "xgnhn", '250', "afgj678.com", 'fg098i')
# s.insert_student("aaaa", "sdfghjhn", '2650', "afzxcv.com", 'qwe3i')
# s.get_student_by_id('2')
# s.delete_student("Maya", "grossman", "we12.com", 'fgh1234')
# s.get_student_by_email("mha.com")
# g.get_all_groups()
# g.get_group_by_id('1')
# g.get_group_by_teacherId('2')
# g.update_group('4', "swimming", '2', "tennis")
# s.update_student("sdfh", "mnw", '300', "fgh6", 'xcvb7', "aaaa", "sdfghjhn", '2650', "afzxcv.com", 'qwe3i')
# s.get_student_by_email_and_password("mha.com", '9o234')




#u.insert_user("v@y.com", "dvidi", 'davidi')
#u.insert_user("t@a.com", "aba", 'origin')
#u.select_all_users()
#u.check_user_by_username("Asaf")
#u.delete_username("Asaf")
#u.check_user_by_username("Asaf")
#user=u.return_user_by_email('u@x.com')
#print(user[0])
#print(user)