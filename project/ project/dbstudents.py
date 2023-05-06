import sqlite3
import hashlib

class students(object):
    def __init__(self, tablename = "students", studentId = "studentId", firstname = "firstname", lastname = "lastname", priceforayear = "priceforayear", email = "email", password = "password"):
        self.__tablename = tablename
        self.__studentId = studentId
        self.__firstname = firstname
        self.__lastname = lastname
        self.__priceforayear = priceforayear
        self.__email = email
        self.__password = password

        conn = sqlite3.connect('test.db')
        print ("Opened database successfully")
        str = "CREATE TABLE IF NOT EXISTS " + self.__tablename + "(" + self.__studentId + " " + "INTEGER PRIMARY KEY AUTOINCREMENT ,"
        str += " " + self.__firstname + " TEXT    NOT NULL ,"
        str += " " + self.__lastname + " TEXT    NOT NULL, "
        str += " " + self.__priceforayear + " TEXT    NOT NULL, "
        str += " " + self.__email + " TEXT    NOT NULL, "
        str += " " + self.__password + " TEXT    NOT NULL) "
        conn.execute(str)
        print("Table created successfully");
        conn.commit()
        conn.close()
    def get_table_name(self):
        return self.__tablename
    def get_all_students(self):
        try:
            conn = sqlite3.connect('test.db')
            print("Opened database successfully");
            str1 = "select*from " + self.__tablename
            print(str1)
            cursor = conn.execute(str1)
            rows = cursor.fetchall()
            arr_students = []
            for row in rows:
                arr_students.append({
                    "studentId": row[0],
                    "firstname": row[1],
                    "lastname": row[2],
                    "priceforayear": row[3],
                    "email": row[4],
                    "password": row[5]
                })
                # str_rows = str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4])
                # arr_students.append(str_rows)
            print(arr_students)
            return arr_students
        except:
            return False

    def get_id_by_name(self, name):
        try:
            conn = sqlite3.connect('test.db')
            print("Opened database successfully")
            firstname, lastname = name.split()
            str1 = f"SELECT {self.__studentId} FROM {self.__tablename} WHERE {self.__firstname}='{firstname}' AND {self.__lastname}='{lastname}'"
            print(str1)
            cursor = conn.execute(str1)
            row = cursor.fetchone()
            if row:
                student_id = row[0]
                print(student_id)
                return student_id
            else:
                print("No student found with that name")
                return None
        except:
            return False
    # def insert_student(self, firstname, lastname, priceforayear, email, password):
    #     conn = sqlite3.connect('test.db')
    #     print("Opened database successfully")
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
    #             str_insert = "INSERT INTO " + self.__tablename + " (" + self.__firstname + "," + self.__lastname + "," + self.__priceforayear + "," + self.__email + "," + self.__password + \
    #                          ") VALUES (" + "'" + firstname + "'" + "," + "'" + lastname + "'" + "," + "'" + priceforayear + "'" + "," + "'" + email + "'" + "," + "'" + password + "');"
    #             print(str_insert)
    #             conn.execute(str_insert)
    #             conn.commit()
    #             conn.close()
    #             print("Record created successfully");
    #             return True
    #         except:
    #             print("Failed to insert user")
    #             return False
    def insert_student(self, firstname, lastname, priceforayear, email, password):
        conn = sqlite3.connect('test.db')
        print("Opened database successfully")
        cursor = conn.execute(f"SELECT * from {self.__tablename} where {self.__email} = '{email}' and {self.__password} = '{password}'")
        row = cursor.fetchall()
        if row:
            print("Exist")
            return "exist"
        else:
            try:
                str_insert = f"INSERT INTO {self.__tablename} ({self.__firstname}, {self.__lastname}, {self.__priceforayear}, {self.__email}, {self.__password}) VALUES ('{firstname}', '{lastname}', '{priceforayear}', '{email}', '{password}');"
                conn.execute(str_insert)
                conn.commit()
                print("Record created successfully")
                return True
            except:
                print("Failed to insert user")
                return False


    def delete_student(self, firstname, lastname, priceforayear, email, password):
        try:
            conn = sqlite3.connect('test.db')
            str_delete = "DELETE  from " + self.__tablename + " where " + self.__firstname + "=" + "'"+str(firstname)+"'" +\
                         ' and ' + self.__lastname + "=" + "'"+str(lastname)+ "'" + ' and ' + self.__priceforayear + "=" + "'"+str(priceforayear) + "'" + ' and ' + self.__email + "=" + "'"+str(email)+ "'" + ' and ' + self.__password + "=" + "'"+str(password) + "'"
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

    def update_student(self, firstname, lastname, priceforayear, email, password, firstname1, lastname1, priceforayear1, email1, password1):
        try:
            conn = sqlite3.connect('test.db')
            str_update = " UPDATE " + self.__tablename + " set "
            str_update += self.__firstname + "=" + "'" + firstname + "',"
            str_update += self.__lastname + "=" + "'" + lastname + "',"
            str_update += self.__priceforayear + "=" + "'" + priceforayear + "',"
            str_update += self.__email + "=" + "'" + email + "',"
            str_update += self.__password + "=" + "'" + password + "'"
            str_update += " WHERE " + self.__firstname + "=" + "'" + firstname1 + "'"
            str_update += " and " + self.__lastname + "=" + "'" + lastname1 + "'"
            str_update += " and " + self.__priceforayear + "=" + "'" + priceforayear1 + "'"
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


    def get_student_by_id(self, studentId):
        try:
            conn = sqlite3.connect('test.db')
            print("Opened database successfully")
            # salt = 'GROSSMAN'
            # salt_password = hashlib.md5(salt.encode('utf-8') + password.encode('utf-8')).hexdigest()
            # print(salt_password)
            # strsql= f"SELECT * from {self.__tablename} where '{self.__email}' = {str(email)} and {self.__password}" \
            #             f" = '{str(salt_password)}"
            # print(strsql)

            strsql = "SELECT * from " + self.__tablename + " where " + self.__studentId + "=" + "'" + str(studentId) + "'"
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

    def get_price_for_student(self, email, password):
        try:
            conn = sqlite3.connect('test.db')
            cursor = conn.execute(
                f"SELECT {self.__priceforayear} FROM {self.__tablename} WHERE {self.__email}='{email}' AND {self.__password}='{password}'")
            row = cursor.fetchone()
            conn.close()
            if row is not None:
                print(row[0])
                return row[0]
            else:
                print("failed")
                return None
        except:
            print("failed")
            return None

    def update_price(self, sum, email, password):
        try:
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            cursor.execute("SELECT priceforayear FROM students WHERE email=? AND password=?", (email, password))
            row = cursor.fetchone()
            print(row)
            # if row is None:
            #     print("Invalid email or password")
            #     return "Invalid email or password"
            priceforayear = int(row[0])
            if priceforayear == 1500:
                print("already payed")
                return "already payed"
            new_priceforayear = priceforayear + int(sum)
            print(new_priceforayear)
            if new_priceforayear > 1500:
                print("Please pay the exact sum of money")
                return "Please pay the exact sum of money"
            elif new_priceforayear == 1500:
                cursor.execute("UPDATE students SET priceforayear=? WHERE email=? AND password=?",
                               (new_priceforayear, email, password))
                conn.commit()
                conn.close()
                print("You paid everything")
                return "You paid everything"
            else:
                to_pay = 1500 - int(new_priceforayear)
                cursor.execute("UPDATE students SET priceforayear=? WHERE email=? AND password=?",
                               (new_priceforayear, email, password))
                conn.commit()
                conn.close()
                print(str(to_pay))
                return str(to_pay)

        except:
            print("Error")
            return "Error"

    def get_all_student_names(self):
        try:
            conn = sqlite3.connect('test.db')
            print("Opened database successfully");
            str1 = "SELECT " + self.__firstname + ", " + self.__lastname + " FROM " + self.__tablename
            print(str1)
            cursor = conn.execute(str1)
            rows = cursor.fetchall()
            arr_students = []
            for row in rows:
                arr_students.append(row[0] + " " + row[1])
            print(arr_students)
            return arr_students
        except:
            return False

    def delete_student_by_id(self,student_id):
        try:
            conn = sqlite3.connect('test.db')
            print("Opened database successfully")
            str1 = "DELETE FROM " + self.__tablename + " WHERE " + self.__studentId + " = ?"
            conn.execute(str1, (student_id,))
            conn.commit()
            conn.close()
            print("Student with ID {} deleted successfully".format(student_id))
            return True
        except:
            return False

    def __str__(self):
        return "table  name is ", self.__tablename


# s = students()
# s.get_id_by_name("dcf qwey")
# s.delete_student_by_id(6)
# s.update_price(1200,"mha.com","9o234")
# s.get_price_for_student("mha.com","9o234")
# s.update_student("fgbh", "shn", '800', "6356xcv.com", 'hdcs2333i',"fgbh", "shn", '9850', "6356xcv.com", 'hdcs2333i')
# s.insert_student("dcf", "qwey", '250', "mha.com", '9o234')
# s.insert_student("bgka", "xgnhn", '250', "afgj678.com", 'fg098i')
# s.insert_student("fgbh", "shn", '9850', "6356xcv.com", 'hdcs2333i')
# s.insert_student("dcghf", "qwegvbhy", '50', "mh89a.com", '9o345234')
# s.get_student_by_id('2')
# s.delete_student("Maya", "grossman", "we12.com", 'fgh1234')
# s.get_student_by_email("mha.com")
# s.get_all_students()
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