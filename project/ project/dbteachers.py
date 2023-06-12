import sqlite3
import hashlib

class teachers(object):
    def __init__(self, tablename = "teachers", teacherId = "teacherId", firstname = "firstname", lastname = "lastname", email = "email", password = "password"):
        self.__tablename = tablename
        self.__teacherId = teacherId
        self.__firstname = firstname
        self.__lastname = lastname
        self.__email = email
        self.__password = password

        conn = sqlite3.connect('test.db')
        print ("Opened database successfully")
        str = "CREATE TABLE IF NOT EXISTS " + self.__tablename + "(" + self.__teacherId + " " + "INTEGER PRIMARY KEY AUTOINCREMENT ,"
        str += " " + self.__firstname + " TEXT    NOT NULL ,"
        str += " " + self.__lastname + " TEXT    NOT NULL, "
        str += " " + self.__email + " TEXT    NOT NULL, "
        str += " " + self.__password + " TEXT    NOT NULL) "
        conn.execute(str)
        print("Table created successfully");
        conn.commit()
        conn.close()
    def get_table_name(self):
        return self.__tablename
    def get_all_teachers(self):
        try:
            conn = sqlite3.connect('test.db')
            print("Opened database successfully");
            str1 = "select*from " + self.__tablename
            print(str1)
            cursor = conn.execute(str1)
            rows = cursor.fetchall()
            arr_teachers = []
            for row in rows:
                arr_teachers.append({
                    "teacherId": row[0],
                    "firstname": row[1],
                    "lastname": row[2],
                    "email": row[3],
                    "password": row[4]
                })
                # str_rows = str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4])
                # arr_teachers.append(str_rows)

            print(arr_teachers)
            return arr_teachers
        except:
            return False

    def get_all_names(self):
        try:
            conn = sqlite3.connect('test.db')
            print("Opened database successfully")
            str1 = "select " + self.__firstname + ", " + self.__lastname + " from " + self.__tablename
            print(str1)
            cursor = conn.execute(str1)
            rows = cursor.fetchall()
            arr_names = []
            for row in rows:
                arr_names.append(row[0] + " " + row[1])
            print(arr_names)
            return arr_names
        except:
            return False

    def get_id_by_name(self, fullname):
        try:
            conn = sqlite3.connect('test.db')
            print("Opened database successfully")
            firstname, lastname = fullname.split()
            str1 = "SELECT " + self.__teacherId + " FROM " + self.__tablename + " WHERE " + self.__firstname + "='" + firstname + "' AND " + self.__lastname + "='" + lastname + "'"
            print(str1)
            cursor = conn.execute(str1)
            row = cursor.fetchone()
            if row is not None:
                teacher_id = row[0]
                print("Teacher ID for " + fullname + " is " + str(teacher_id))
                return teacher_id
            else:
                print("No teacher found with name " + fullname)
                return False
        except:
            return False

    # def insert_teacher(self, firstname, lastname, email, password):
    #     conn = sqlite3.connect('test.db')
    #     print("Opened database successfully")
    #
    #     str_check = f"SELECT * from {self.__tablename} where '{email}' = {self.__email} and " \
    #                 f"'{password}' = {self.__password}"
    #     print(str_check)
    #     cursor = conn.execute(str_check)
    #     row = cursor.fetchall()
    #     if row:
    #         print("Exist")
    #         return "exist"
    #     else:
    #         try:
    #             # salt = 'GROSSMAN'
    #             # salt_password = hashlib.md5(salt.encode('utf-8') + password.encode('utf-8')).hexdigest()
    #             # print(salt_password)
    #             str_insert = "INSERT INTO " + self.__tablename + " (" + self.__firstname + "," + self.__lastname + "," + self.__email + "," + self.__password + \
    #                          ") VALUES (" + "'" + firstname + "'" + "," + "'" + lastname + "'" + "," + "'" + email + "'" + "," + "'" + password + "');"
    #             print(str_insert)
    #             conn.execute(str_insert)
    #             conn.commit()
    #             conn.close()
    #             print("Record created successfully");
    #             return True
    #         except:
    #             print("Failed to insert user")
    #             return False
    # def insert_teacher(self, firstname, lastname, email, password):
    #     conn = sqlite3.connect('test.db')
    #     print("Opened database successfully")
    #
    #     str_check = f"SELECT * from {self.__tablename} where {self.__email} = '{email}' and {self.__password} = '{password}'"
    #     cursor = conn.execute(str_check)
    #     row = cursor.fetchall()
    #     if row:
    #         print("Exist")
    #         return "exist"
    #     else:
    #         try:
    #             str_insert = f"INSERT INTO {self.__tablename} ({self.__firstname}, {self.__lastname}, {self.__email}, {self.__password}) VALUES ('{firstname}', '{lastname}', '{email}', '{password}');"
    #             conn.execute(str_insert)
    #             conn.commit()
    #             conn.close()
    #             print("Record created successfully");
    #             return True
    #         except:
    #             print("Failed to insert user")
    #             return False

    def insert_teacher(self, firstname, lastname, email, password):
        conn = sqlite3.connect('test.db')
        print("Opened database successfully")

        str_check = f"SELECT * from {self.__tablename} where {self.__email} = '{email}'"
        cursor = conn.execute(str_check)
        row = cursor.fetchone()
        if row:
            hashed_password = row[self.__password]  # Get the hashed password from the database
        else:
            hashed_password = None

        salt = 'GROSSMAN'  # Default salt value

        if hashed_password and hashed_password == hashlib.md5(
                salt.encode('utf-8') + password.encode('utf-8')).hexdigest():
            print("Exist")
            return "exist"

        try:
            # Hash the password
            salt_password = hashlib.md5(salt.encode('utf-8') + password.encode('utf-8')).hexdigest()

            str_insert = f"INSERT INTO {self.__tablename} ({self.__firstname}, {self.__lastname}, {self.__email}, {self.__password}) VALUES ('{firstname}', '{lastname}', '{email}', '{salt_password}');"
            conn.execute(str_insert)
            conn.commit()
            conn.close()
            print("Record created successfully")
            return True
        except:
            print("Failed to insert user")
            return False

    def delete_teacher(self, firstname, lastname, email, password):
        try:
            conn = sqlite3.connect('test.db')
            str_delete = "DELETE  from " + self.__tablename + " where " + self.__firstname + "=" + "'"+str(firstname)+"'" +\
                         ' and ' + self.__lastname + "=" + "'"+str(lastname)+ "'" + ' and ' + self.__email + "=" + "'"+str(email)+ "'" + ' and ' + self.__password + "=" + "'"+str(password) + "'"
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

    def update_teacher(self, firstname, lastname, email, password, firstname1, lastname1, email1, password1):
        try:
            conn = sqlite3.connect('test.db')
            str_update = " UPDATE " + self.__tablename + " set "
            str_update += self.__firstname + "=" + "'" + firstname + "',"
            str_update += self.__lastname + "=" + "'" + lastname + "',"
            str_update += self.__email + "=" + "'" + email + "',"
            str_update += self.__password + "=" + "'" + password + "'"
            str_update += " WHERE " + self.__firstname + "=" + "'" + firstname1 + "'"
            str_update += " and " + self.__lastname + "=" + "'" + lastname1 + "'"
            str_update += " and " + self.__email + "=" + "'" + email1 + "'"
            str_update += " and " + self.__password + "=" + "'" + password1 + "'"

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


    def get_teacher_by_id(self, teacherId):
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
            arr_teachers = []
            if row:
                str_rows = str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4])
                # return [row[0], row[1], row[2], row[3], row[4]]
                arr_teachers.append(str_rows)
                print(arr_teachers)

                return arr_teachers
                # return [row[0], row[1], row[2], row[3], row[4]]

            else:
                print("Failed to find user")
                return False
            conn.commit()
            conn.close()
        except:
            return False


    def get_teacher_by_email(self, email):
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
            arr_teachers = []
            if row:
                str_rows = str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4])
                # return [row[0], row[1], row[2], row[3], row[4]]
                arr_teachers.append(str_rows)
                print(arr_teachers)

                return arr_teachers

            else:
                print("Failed to find user")
                return False
            conn.commit()
            conn.close()
        except:
            return False


    # def get_teacher_by_email_and_password(self, email, password):
    #     try:
    #         conn = sqlite3.connect('test.db')
    #         print("Opened database successfully")
    #         # salt = 'GROSSMAN'
    #         # salt_password = hashlib.md5(salt.encode('utf-8') + password.encode('utf-8')).hexdigest()
    #         # print(salt_password)
    #         # strsql= f"SELECT * from {self.__tablename} where '{self.__email}' = {str(email)} and {self.__password}" \
    #         #             f" = '{str(salt_password)}"
    #         # print(strsql)
    #
    #         strsql = "SELECT * from " + self.__tablename + " where " + self.__email + "=" + "'" + str(email) + "'" + ' and ' + self.__password + "=" + "'" + str(password) + "'"
    #         print(strsql)
    #         cursor = conn.execute(strsql)
    #         row = cursor.fetchone()
    #         if row:
    #             str_rows = str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4])
    #             # return [row[0], row[1], row[2], row[3], row[4]]
    #             arr_teachers = str_rows.split(" ")
    #             print(arr_teachers)
    #             return arr_teachers
    #
    #         else:
    #             print("Failed to find user")
    #             return False
    #         conn.commit()
    #         conn.close()
    #     except:
    #         return False
    import hashlib

    def get_teacher_by_email_and_password(self, email, password):
        try:
            conn = sqlite3.connect('test.db')
            print("Opened database successfully")

            query = f"SELECT * FROM {self.__tablename} WHERE {self.__email} = '{email}' AND {self.__password} = '{password}'"
            cursor = conn.execute(query)
            row = cursor.fetchone()
            print(row)
            conn.close()

            if row:
                stored_password = row[4]  # Assuming the password is in the fourth column
                print(stored_password)

                # Check if the password is already hashed
                if password == stored_password:
                    # Password matches, return the teacher's details
                    str_rows = " ".join(str(value) for value in row)
                    arr_teachers = str_rows.split(" ")
                    print(arr_teachers)
                    return arr_teachers

                # Hash the password if it's not already hashed
                salt = 'GROSSMAN'
                salt_password = hashlib.md5(salt.encode('utf-8') + password.encode('utf-8')).hexdigest()

                if salt_password == stored_password:
                    # Password matches, return the teacher's details
                    str_rows = " ".join(str(value) for value in row)
                    arr_teachers = str_rows.split(" ")
                    print(arr_teachers)
                    return arr_teachers

            print("Failed to find user")
            return False
        except:
            return False

    # def get_teacher_by_group_name(self, nameofgroup):
    #     try:
    #         conn = sqlite3.connect('test.db')
    #         str_select = "SELECT * FROM {} INNER JOIN groups ON {}.{}=groups.{} WHERE groups.{}=?".format(
    #             self.__tablename, self.__tablename, self.__teacherId, "teacherId", "nameofgroup")
    #         cursor = conn.execute(str_select, (nameofgroup,))
    #         row = cursor.fetchone()
    #         if row:
    #             print(row[0], row[1], row[2], row[3], row[4])
    #             return [row[0], row[1], row[2], row[3], row[4]]
    #         else:
    #             return False
    #         conn.commit()
    #         conn.close()
    #     except:
    #         return False
    def get_teacher_by_group_name(self, nameofgroup):
        try:
            conn = sqlite3.connect('test.db')
            str_select = "SELECT {}.*, groups.{} FROM {} INNER JOIN groups ON {}.{}=groups.{} WHERE groups.{}=?".format(
                self.__tablename, self.__teacherId, self.__tablename, self.__tablename, self.__teacherId, "teacherId",
                "nameofgroup")
            cursor = conn.execute(str_select, (nameofgroup,))
            rows = cursor.fetchall()
            results = [[row[1], row[2]] for row in rows]
            conn.commit()
            conn.close()
            print(results)
            return results
        except:
            print("False")
            return False

    def get_teacher_name_by_id(self, teacherId):
        try:
            conn = sqlite3.connect('test.db')
            str_select = "SELECT firstname, lastname FROM {} WHERE {}=?".format(self.__tablename, self.__teacherId)
            cursor = conn.execute(str_select, (teacherId,))
            rows = cursor.fetchall()
            results = [(row[0], row[1]) for row in rows]
            conn.commit()
            conn.close()
            print(results)
            return results
        except:
            print("False")
            return False

    def get_name_by_email_and_password(self, email, password):
        try:
            conn = sqlite3.connect('test.db')
            print("Opened database successfully")

            strsql = "SELECT " + self.__firstname + ", " + self.__lastname + " from " + self.__tablename + " where " + self.__email + "=" + "'" + email + "'" + ' and ' + self.__password + "=" + "'" + password + "'"
            print(strsql)

            cursor = conn.execute(strsql)
            row = cursor.fetchone()

            if row:
                first_name = row[0]
                last_name = row[1]
                print(first_name, last_name)
                return (first_name, last_name)
            else:
                print("failed")
                return "failed"

            conn.commit()
            conn.close()

        except:
            print("failed")
            return "failed"

    def delete_teacher_by_id(self, teacher_id):
        try:
            conn = sqlite3.connect('test.db')
            print("Opened database successfully")
            str1 = "DELETE FROM " + self.__tablename + " WHERE " + self.__teacherId + " = ?"
            conn.execute(str1, (teacher_id,))
            conn.commit()
            conn.close()
            print("Teacher with ID {} deleted successfully".format(teacher_id))
            return True
        except:
            return False

    # def get_teacher_name(self, email, password):
    #     try:
    #         conn = sqlite3.connect('test.db')
    #         print("Opened database successfully")
    #         query = f"SELECT firstname, lastname FROM teachers WHERE email = '{email}' AND password = '{password}'"
    #         cursor = conn.execute(query)
    #         result = cursor.fetchone()
    #         conn.close()
    #
    #         if result:
    #             print(result[0], result[1])
    #             return result[0], result[1]
    #         else:
    #             return False
    #     except:
    #         return False

    def get_teacher_name(self, email, password):
        try:
            conn = sqlite3.connect('test.db')
            print("Opened database successfully")

            # Hash the password
            salt = 'GROSSMAN'
            salt_password = hashlib.md5(salt.encode('utf-8') + password.encode('utf-8')).hexdigest()

            query = f"SELECT firstname, lastname FROM teachers WHERE email = '{email}' AND password = '{salt_password}'"
            cursor = conn.execute(query)
            result = cursor.fetchone()
            conn.close()

            if result:
                print(result[0], result[1])
                return result[0], result[1]
            else:
                return False
        except:
            return False

    # def check_teacher_exists(self, email, password):
    #     try:
    #         conn = sqlite3.connect('test.db')
    #         print("Opened database successfully")
    #
    #         query = f"SELECT * FROM teachers WHERE email = '{email}' AND password = '{password}'"
    #         cursor = conn.execute(query)
    #         row = cursor.fetchone()
    #         conn.close()
    #
    #         if row:
    #             print("Teacher exists")
    #             return True
    #         else:
    #             print("Teacher does not exist")
    #             return False
    #     except:
    #         print("Failed to check teacher existence")
    #         return False
    import hashlib

    import hashlib

    def check_teacher_exists(self, email, password):
        try:
            conn = sqlite3.connect('test.db')
            print("Opened database successfully")

            query = f"SELECT * FROM {self.__tablename} WHERE email = '{email}' AND password = '{password}'"
            cursor = conn.execute(query)
            row = cursor.fetchone()
            print(row)
            conn.close()

            if row:
                stored_password = row[4]  # Assuming the hashed password is in the fifth column
                print(stored_password)

                # Check if the password is already hashed
                if password == stored_password:
                    print("Teacher exists")
                    return True

                # Hash the password if it's not already hashed
                salt = 'GROSSMAN'
                salt_password = hashlib.md5(salt.encode('utf-8') + password.encode('utf-8')).hexdigest()

                if salt_password == stored_password:
                    print("Teacher exists")
                    return True
            else:
                print("Teacher does not exist")
                return False
        except:
            print("Failed to check teacher existence")
            return False

    def hash_and_update_password(self, email, password):
        try:
            conn = sqlite3.connect('test.db')
            print("Opened database successfully")

            # Retrieve the teacher from the database
            query = f"SELECT * FROM teachers WHERE email = '{email}'"
            cursor = conn.execute(query)
            row = cursor.fetchone()
            if row:
                teacher_id = row[0]
                print("Teacher found:", teacher_id)

                # Hash the provided password
                salt = 'GROSSMAN'
                hashed_password = hashlib.md5(salt.encode('utf-8') + password.encode('utf-8')).hexdigest()

                # Update the hashed password in the database
                update_query = "UPDATE teachers SET password = ? WHERE teacherid = ?"
                conn.execute(update_query, (hashed_password, teacher_id))
                conn.commit()

                print("Password updated successfully")
                conn.close()
                return True
            else:
                print("Teacher not found")
                conn.close()
                return False
        except:
            print("Failed to update password")
            return False

    def __str__(self):
        return "table  name is ", self.__tablename


t=teachers()
t.hash_and_update_password("mha.com","9o234")
# t.hash_and_update_password("qwe56","zxc567")
# arr = t.get_teacher_name("qwe56", "zxc567")
# print(arr[0])
# t.get_id_by_name("lilya qwew")
# t.get_name_by_email_and_password("qwe56", 'zxc567')
# t.get_all_names()
# t.delete_teacher_by_id(79)
# arr = t.get_teacher_name_by_id(3)
# print(arr[0])
# t.get_teacher_by_group_name("kids tennis")
# t.get_teacher_by_group_name("swimming")
# t.insert_teacher("lilya", "qwew", "qwe56", 'zxc567')
# t.insert_teacher("gaya", "tyu", "re34.com", '1234')
# t.insert_teacher("anna", "sdxcf", "dgfcgv123.com", 'qwr567')
# t.insert_teacher("vb", "zsdfv", "d36677.com", '23456sdfg7')
# t.get_teacher_by_id('4')
# t.delete_teacher("Maya", "grossman", "we12.com", 'fgh1234')
# t.get_teacher_by_email("d3.com")
# t.get_all_teachers()
# t.update_teacher("ddf", "sdfvb", "qdwf.com", '64897', "gaya", "tyu", "re34.com", '1234')
# t.get_teacher_by_email_and_password("dgfcgv123.com", 'qwr567')
# arr_teachers = t.get_teacher_by_email_and_password("qwe56", 'zxc567')
# print(arr_teachers[0])







#u.insert_user("v@y.com", "dvidi", 'davidi')
#u.insert_user("t@a.com", "aba", 'origin')
#u.select_all_users()
#u.check_user_by_username("Asaf")
#u.delete_username("Asaf")
#u.check_user_by_username("Asaf")
#user=u.return_user_by_email('u@x.com')
#print(user[0])
#print(user)