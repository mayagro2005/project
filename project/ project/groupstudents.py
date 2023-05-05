import sqlite3
import hashlib

class groupstudents(object):
    def __init__(self, tablename = "groupstudents", groupstudentId = "groupstudentId", studentId = "studentId", groupId = "groupId"):
        self.__tablename = tablename
        self.__groupstudentId = groupstudentId
        self.__studentId = studentId
        self.__groupId = groupId


        conn = sqlite3.connect('test.db')
        print ("Opened database successfully")
        str = "CREATE TABLE IF NOT EXISTS " + self.__tablename + "(" + self.__groupstudentId + " " + "INTEGER PRIMARY KEY AUTOINCREMENT ,"
        str += " " + self.__studentId + " TEXT    NOT NULL ,"
        str += " " + self.__groupId + " TEXT    NOT NULL) "
        conn.execute(str)
        print("Table created successfully");
        conn.commit()
        conn.close()
    def get_table_name(self):
        return self.__tablename

    def insert_student_to_group(self, studentId, groupId):
        conn = sqlite3.connect('test.db')
        print("Opened database successfully")
        str_check = f"SELECT * from {self.__tablename} where '{studentId}' = {self.__studentId} and " \
                    f"'{groupId}' = {self.__groupId}"
        print(str_check)
        cursor = conn.execute(str_check)
        row = cursor.fetchall()
        if row:
            print("Exist")
            return True
        else:
            try:
                # salt = 'GROSSMAN'
                # salt_password = hashlib.md5(salt.encode('utf-8') + password.encode('utf-8')).hexdigest()
                # print(salt_password)
                str_insert = "INSERT INTO " + self.__tablename + " (" + self.__studentId + "," + self.__groupId + \
                             ") VALUES (" + "'" + studentId + "'" + "," + "'" + groupId + "');"
                print(str_insert)
                conn.execute(str_insert)
                conn.commit()
                conn.close()
                print("Record created successfully");
                return True
            except:
                print("Failed to insert user")
                return False

    def delete_student_from_group(self, studentId, groupId):
        conn = sqlite3.connect('test.db')
        print("Opened database successfully")
        try:
            str_delete = "DELETE  from " + self.__tablename + " where " + self.__studentId + "=" + "'" + str(studentId) + "'" + \
            ' and ' + self.__groupId + "=" + "'" + str(
                groupId) + "'"
            print(str_delete)
            conn.execute(str_delete)
            conn.commit()
            conn.close()
            print("Record deleted successfully")
            return "Success"
        except:
            return "Failed to delete user"

    # def get_students_by_group_id(self, groupId):
    #     conn = sqlite3.connect('test.db')
    #     print("Opened database successfully")
    #
    #     str_select = "SELECT * from " + self.__tablename + " where " + self.__groupId + "=" + "'" + str(groupId) + "'"
    #     print(str_select)
    #     cursor = conn.execute(str_select)
    #     rows = cursor.fetchall()
    #     if rows:
    #         students = []
    #         for row in rows:
    #             student = {
    #                 "studentId": row[0],
    #                 "teacherId": row[1],
    #                 "nameofgroup": row[2]
    #             }
    #             students.append(student)
    #         print(students)
    #         return students
    #     else:
    #         return "No students found for this group"

    # def get_student_name_by_group_name(self, group_name):
    #     try:
    #         conn = sqlite3.connect('test.db')
    #         str_select = f"SELECT students.firstname, students.lastname FROM students INNER JOIN groupstudents ON students.studentId = groupstudents.studentId INNER JOIN groups ON groups.groupId = groupstudents.groupId WHERE groups.nameofgroup = '{group_name}'"
    #         cursor = conn.execute(str_select)
    #         rows = cursor.fetchone()
    #         names = []
    #         for row in rows:
    #             names.append({
    #                 "firstname": row[0],
    #                 "lastname": row[1]
    #             })
    #         print(names)
    #         return names
    #     except:
    #         return False

    def get_student_name_by_group_name(self, group_name):
        try:
            conn = sqlite3.connect('test.db')
            str_select = f"SELECT students.firstname, students.lastname FROM students INNER JOIN groupstudents ON students.studentId = groupstudents.studentId INNER JOIN groups ON groups.groupId = groupstudents.groupId WHERE groups.nameofgroup = '{group_name}'"
            cursor = conn.execute(str_select)
            rows = cursor.fetchall()
            names = []
            for row in rows:
                names.append({
                    "firstname": row[0],
                    "lastname": row[1]
                })
            print(names)
            return names
        except:
            return False

    def get_all_groupsstudents(self):
        conn = sqlite3.connect('test.db')
        str_select = f"SELECT * FROM {self.__tablename}"
        cursor = conn.execute(str_select)
        rows = cursor.fetchall()
        if rows:
            groupstudents = []
            for row in rows:
                groupstudents1 = {
                    "groupstudentsId": row[0],
                    "studentId": row[1],
                    "groupId": row[2]
                }
                groupstudents.append(groupstudents1)
            print(groupstudents)
            return groupstudents
        else:
            return None

    def get_student_names_by_group_id(self, groupId):
        try:
            conn = sqlite3.connect('test.db')
            str_select = f"SELECT firstname, lastname FROM students INNER JOIN {self.__tablename} ON students.studentId = {self.__tablename}.studentId WHERE {self.__groupId} = '{groupId}'"
            cursor = conn.execute(str_select)
            rows = cursor.fetchall()
            names = []
            for row in rows:
                names.append({
                    "firstname": row[0],
                    "lastname": row[1]
                })
            print(names)
            return names
        except:
            return False

    # def insert_student_to_group2(self, nameofgroup, startH, endH,
    #                              lessonDay, teacher_name, student_firstname, student_lastname):
    #     try:
    #         # Establish a new database connection
    #         conn = sqlite3.connect('test.db')
    #
    #         # Create a cursor object to execute SQL queries
    #         cursor = conn.cursor()
    #
    #         # Get teacher_id by splitting teacher_name into first and last name
    #         teacher_firstname, teacher_lastname = teacher_name.split()
    #         print(teacher_firstname,teacher_lastname)
    #         cursor.execute("SELECT teacherId FROM teachers WHERE firstname=? AND lastname=?",
    #                        (teacher_firstname, teacher_lastname))
    #         teacher_id = cursor.fetchone()[0]
    #         print(teacher_id)
    #
    #         # Get group_id using the given parameters
    #         print(nameofgroup, startH, endH, lessonDay, teacher_id)
    #
    #         # Get group_id using the given parameters
    #         cursor.execute(
    #             "SELECT groups.groupId FROM groups JOIN groupstime ON groups.groupId=groupstime.groupId WHERE nameofgroup=? AND startH=? AND endH=? AND lessonDay=? AND groups.teacherId=?",
    #             (nameofgroup, startH, endH, lessonDay, teacher_id))
    #         group_id = cursor.fetchone()[0]
    #         print(group_id)
    #         # Get student_id using the given parameters
    #         cursor.execute("SELECT studentId FROM students WHERE firstname=? AND lastname=?",
    #                        (student_firstname, student_lastname))
    #         student_id = cursor.fetchone()[0]
    #         print(student_id)
    #
    #         # Insert the new record into groupstudents table
    #         cursor.execute("INSERT INTO groupstudents (studentId, groupId) VALUES (?, ?)", (student_id, group_id))
    #
    #         # Commit the changes to the database
    #         conn.commit()
    #
    #         print("Student inserted successfully to group.")
    #         return "Success"
    #     except Exception as e:
    #         print("Error inserting student to group:", e)
    #         return "error"
    def insert_student_to_group2(self, nameofgroup, startH, endH,
                                 lessonDay, teacher_name, student_firstname, student_lastname):
        try:
            # Establish a new database connection
            conn = sqlite3.connect('test.db')

            # Create a cursor object to execute SQL queries
            cursor = conn.cursor()

            # Get teacher_id by splitting teacher_name into first and last name
            teacher_firstname, teacher_lastname = teacher_name.split()
            cursor.execute("SELECT teacherId FROM teachers WHERE firstname=? AND lastname=?",
                           (teacher_firstname, teacher_lastname))
            teacher_id = cursor.fetchone()[0]

            # Get group_id using the given parameters
            cursor.execute(
                "SELECT groups.groupId FROM groups JOIN groupstime ON groups.groupId=groupstime.groupId WHERE nameofgroup=? AND startH=? AND endH=? AND lessonDay=? AND groups.teacherId=?",
                (nameofgroup, startH, endH, lessonDay, teacher_id))
            group_id = cursor.fetchone()[0]

            # Get student_id using the given parameters
            cursor.execute("SELECT studentId FROM students WHERE firstname=? AND lastname=?",
                           (student_firstname, student_lastname))
            student_id = cursor.fetchone()

            if student_id is not None:
                # Check if student already exists in the group
                cursor.execute("SELECT * FROM groupstudents WHERE studentId=? AND groupId=?", (student_id[0], group_id))
                existing_student = cursor.fetchone()

                if existing_student is not None:
                    print("Student already exists in group.")
                    return "Student exists"


            # Insert the new record into groupstudents table
            cursor.execute("INSERT INTO groupstudents (studentId, groupId) VALUES (?, ?)", (student_id[0], group_id))

            # Commit the changes to the database
            conn.commit()

            print("Student inserted successfully to group.")
            return "Success"

        except Exception as e:
            print("Error inserting student to group:", e)
            return "error"

    # def delete_student_to_group2(self, nameofgroup, startH, endH,
    #                              lessonDay, teacher_name, student_firstname, student_lastname):
    #     try:
    #         # Establish a new database connection
    #         conn = sqlite3.connect('test.db')
    #
    #         # Create a cursor object to execute SQL queries
    #         cursor = conn.cursor()
    #
    #         # Get teacher_id by splitting teacher_name into first and last name
    #         teacher_firstname, teacher_lastname = teacher_name.split()
    #         cursor.execute("SELECT teacherId FROM teachers WHERE firstname=? AND lastname=?",
    #                        (teacher_firstname, teacher_lastname))
    #         teacher_id = cursor.fetchone()[0]
    #
    #         # Get group_id using the given parameters
    #         cursor.execute(
    #             "SELECT groups.groupId FROM groups JOIN groupstime ON groups.groupId=groupstime.groupId WHERE nameofgroup=? AND startH=? AND endH=? AND lessonDay=? AND groups.teacherId=?",
    #             (nameofgroup, startH, endH, lessonDay, teacher_id))
    #         group_id = cursor.fetchone()[0]
    #
    #         # Get student_id using the given parameters
    #         cursor.execute("SELECT studentId FROM students WHERE firstname=? AND lastname=?",
    #                        (student_firstname, student_lastname))
    #         student_id = cursor.fetchone()[0]
    #
    #         # Delete the record from groupstudents table
    #         cursor.execute("DELETE FROM groupstudents WHERE studentId=? AND groupId=?", (student_id, group_id))
    #
    #         # Commit the changes to the database
    #         conn.commit()
    #
    #         print("Student deleted successfully from group.")
    #         return "Success"
    #     except Exception as e:
    #         print("Error deleting student from group:", e)
    #         return "error"
    def delete_student_to_group2(self, nameofgroup, startH, endH,
                                 lessonDay, teacher_name, student_firstname, student_lastname):
        try:
            # Establish a new database connection
            conn = sqlite3.connect('test.db')

            # Create a cursor object to execute SQL queries
            cursor = conn.cursor()

            # Get teacher_id by splitting teacher_name into first and last name
            teacher_firstname, teacher_lastname = teacher_name.split()
            cursor.execute("SELECT teacherId FROM teachers WHERE firstname=? AND lastname=?",
                           (teacher_firstname, teacher_lastname))
            teacher_id = cursor.fetchone()[0]

            # Get group_id using the given parameters
            cursor.execute(
                "SELECT groups.groupId FROM groups JOIN groupstime ON groups.groupId=groupstime.groupId WHERE nameofgroup=? AND startH=? AND endH=? AND lessonDay=? AND groups.teacherId=?",
                (nameofgroup, startH, endH, lessonDay, teacher_id))
            group_id = cursor.fetchone()[0]

            # Get student_id using the given parameters
            cursor.execute("SELECT studentId FROM students WHERE firstname=? AND lastname=?",
                           (student_firstname, student_lastname))
            student_id = cursor.fetchone()[0]

            # Check if the student is in the group
            cursor.execute("SELECT * FROM groupstudents WHERE studentId=? AND groupId=?", (student_id, group_id))
            if cursor.fetchone() is None:
                print("You are not in the group")
                return "You are not in the group"

            # Delete the record from groupstudents table
            cursor.execute("DELETE FROM groupstudents WHERE studentId=? AND groupId=?", (student_id, group_id))

            # Commit the changes to the database
            conn.commit()

            print("Student deleted successfully from group.")
            return "Success"
        except Exception as e:
            print("Error deleting student from group:", e)
            return "error"

    def get_students_from_group2(self, nameofgroup, startH, endH, lessonDay, teacher_name):
        try:
            # Establish a new database connection
            conn = sqlite3.connect('test.db')

            # Create a cursor object to execute SQL queries
            cursor = conn.cursor()

            # Get teacher_id by splitting teacher_name into first and last name
            teacher_firstname, teacher_lastname = teacher_name.split()
            cursor.execute("SELECT teacherId FROM teachers WHERE firstname=? AND lastname=?",
                           (teacher_firstname, teacher_lastname))
            teacher_id = cursor.fetchone()[0]

            # Get group_id using the given parameters
            cursor.execute("SELECT g.groupId FROM groups g JOIN groupstime gt ON g.groupId=gt.groupId \
                            WHERE g.nameofgroup=? AND gt.startH=? AND gt.endH=? AND gt.lessonDay=? AND g.teacherId=?",
                           (nameofgroup, startH, endH, lessonDay, teacher_id))
            group_id = cursor.fetchone()[0]

            # Get the first and last name of students in the group
            cursor.execute("SELECT s.firstname, s.lastname FROM students s \
                            JOIN groupstudents gs ON s.studentId=gs.studentId \
                            WHERE gs.groupId=?", (group_id,))
            students = cursor.fetchall()

            # Close the cursor and database connection
            cursor.close()
            conn.close()

            print("Students retrieved successfully from group and lesson.")
            print(students)
            return students
        except Exception as e:
            print("Error retrieving students from group and lesson:", e)
            return "error"

    # def check_student_in_group(self, nameofgroup, startH, endH, lessonDay, teacher_name, student_firstname, student_lastname):
    #     try:
    #         # Establish a new database connection
    #         conn = sqlite3.connect('test.db')
    #
    #         # Create a cursor object to execute SQL queries
    #         cursor = conn.cursor()
    #
    #         # Get teacher_id by splitting teacher_name into first and last name
    #         teacher_firstname, teacher_lastname = teacher_name.split()
    #         cursor.execute("SELECT teacherId FROM teachers WHERE firstname=? AND lastname=?",
    #                        (teacher_firstname, teacher_lastname))
    #         teacher_id = cursor.fetchone()[0]
    #
    #         # Get group_id using the given parameters
    #         cursor.execute(
    #             "SELECT groups.groupId FROM groups JOIN groupstime ON groups.groupId=groupstime.groupId WHERE nameofgroup=? AND startH=? AND endH=? AND lessonDay=? AND groups.teacherId=?",
    #             (nameofgroup, startH, endH, lessonDay, teacher_id))
    #         group_id = cursor.fetchone()[0]
    #
    #         # Get student_id using the given parameters
    #         cursor.execute("SELECT studentId FROM students WHERE firstname=? AND lastname=?",
    #                        (student_firstname, student_lastname))
    #         student_id = cursor.fetchone()
    #
    #         if student_id is not None:
    #             # Check if student already exists in the group
    #             cursor.execute("SELECT * FROM groupstudents WHERE studentId=? AND groupId=?", (student_id[0], group_id))
    #             existing_student = cursor.fetchone()
    #
    #             if existing_student is not None:
    #                 print("Student exists in group.")
    #                 return True
    #             else:
    #                 print("Student does not exist in group.")
    #                 return False
    #         else:
    #             print("Student not found.")
    #             return False
    #
    #     except Exception as e:
    #         print("Error checking student in group:", e)
    #         return False
    # def check_student_in_group(self, nameofgroup, startH, endH, lessonDay, teacher_name, student_firstname,
    #                            student_lastname):
    #     try:
    #         # Establish a new database connection
    #         conn = sqlite3.connect('test.db')
    #
    #         # Create a cursor object to execute SQL queries
    #         cursor = conn.cursor()
    #
    #         # Get teacher_id by splitting teacher_name into first and last name
    #         teacher_firstname, teacher_lastname = teacher_name.split()
    #         cursor.execute("SELECT teacherId FROM teachers WHERE firstname=? AND lastname=?",
    #                        (teacher_firstname, teacher_lastname))
    #         teacher_id = cursor.fetchone()[0]
    #
    #         # Get group_id using the given parameters
    #         cursor.execute(
    #             "SELECT groups.groupId FROM groups JOIN groupstime ON groups.groupId=groupstime.groupId WHERE nameofgroup=? AND startH=? AND endH=? AND lessonDay=? AND groups.teacherId=?",
    #             (nameofgroup, startH, endH, lessonDay, teacher_id))
    #         group_id = cursor.fetchone()[0]
    #
    #         # Get student_id using the given parameters
    #         cursor.execute("SELECT studentId FROM students WHERE firstname=? AND lastname=?",
    #                        (student_firstname, student_lastname))
    #         student = cursor.fetchone()
    #
    #         if student is not None:
    #             student_id = student[0]
    #             # Check if student already exists in the group
    #             cursor.execute("SELECT * FROM groupstudents WHERE studentId=? AND groupId=?", (student_id, group_id))
    #             existing_student = cursor.fetchone()
    #
    #             if existing_student is not None:
    #                 print("Student exists in group.")
    #                 return True
    #             else:
    #                 print("Student does not exist in group.")
    #                 return False
    #         else:
    #             print("Student not found.")
    #             return False
    #
    #     except Exception as e:
    #         print("Error checking student in group:", e)
    #         return False
    def check_student_in_group(self, nameofgroup, startH, endH, lessonDay, teacher_name, student_firstname,
                               student_lastname):
        try:
            # Establish a new database connection
            conn = sqlite3.connect('test.db')

            # Create a cursor object to execute SQL queries
            cursor = conn.cursor()

            # Get teacher_id by splitting teacher_name into first and last name
            teacher_firstname, teacher_lastname = teacher_name.split()
            cursor.execute("SELECT teacherId FROM teachers WHERE firstname=? AND lastname=?",
                           (teacher_firstname, teacher_lastname))
            teacher_id = cursor.fetchone()[0]

            # Get group_id using the given parameters
            cursor.execute(
                "SELECT groups.groupId FROM groups JOIN groupstime ON groups.groupId=groupstime.groupId WHERE nameofgroup=? AND startH=? AND endH=? AND lessonDay=? AND groups.teacherId=?",
                (nameofgroup, startH, endH, lessonDay, teacher_id))
            group_id = cursor.fetchone()

            # if group_id is not None:
            group_id = group_id[0]
            # Get student_id using the given parameters
            cursor.execute("SELECT studentId FROM students WHERE firstname=? AND lastname=?",
                           (student_firstname, student_lastname))
            student = cursor.fetchone()

                # if student is not None:
            student_id = student[0]
            # Check if student already exists in the group
            cursor.execute("SELECT * FROM groupstudents WHERE studentId=? AND groupId=?",
                           (student_id, group_id))
            existing_student = cursor.fetchone()

            if existing_student is not None:
                print("Student exists in group.")
                return True
            else:
                print("Student does not exist in group.")
                return False

        except Exception as e:
            print("Error checking student in group:", e)
            return False

    def check_if_student_in_group(self, nameofgroup, startH, endH, lessonDay, teacher_name, student_firstname,
                                  student_lastname):
        try:
            # Establish a new database connection
            conn = sqlite3.connect('test.db')

            # Create a cursor object to execute SQL queries
            cursor = conn.cursor()

            # Get teacher_id by splitting teacher_name into first and last name
            teacher_firstname, teacher_lastname = teacher_name.split()
            cursor.execute("SELECT teacherId FROM teachers WHERE firstname=? AND lastname=?",
                           (teacher_firstname, teacher_lastname))
            teacher_id = cursor.fetchone()[0]

            # Get group_id using the given parameters
            cursor.execute(
                "SELECT groups.groupId FROM groups JOIN groupstime ON groups.groupId=groupstime.groupId WHERE nameofgroup=? AND startH=? AND endH=? AND lessonDay=? AND groups.teacherId=?",
                (nameofgroup, startH, endH, lessonDay, teacher_id))
            group_id = cursor.fetchone()[0]

            # Get student_id using the given parameters
            cursor.execute("SELECT studentId FROM students WHERE firstname=? AND lastname=?",
                           (student_firstname, student_lastname))
            student_id = cursor.fetchone()[0]

            # Check if the student is in the group
            cursor.execute("SELECT * FROM groupstudents WHERE studentId=? AND groupId=?", (student_id, group_id))
            if cursor.fetchone() is None:
                print("Student is not in group.")
                return False

            print("Student is in group.")
            return True

        except Exception as e:
            print("Error checking if student is in group:", e)
            return False

    def __str__(self):
        return "table  name is ", self.__tablename


# # 'kids tennis', '18:30', '19:30', 'Wednesday', 'lilya qwew', 'dcf', 'qwey'
g = groupstudents()
# g.insert_student_to_group2('kids tennis', '16:00', '17:30', 'Tuesday', 'lilya qwew', 'dcf', 'qwey')
# g.delete_student_to_group2('kids tennis', '16:00', '17:30', 'Tuesday', 'lilya qwew', 'dcf', 'qwey')
# g.check_student_in_group('kids tennis', '17:30', '18:30', 'Monday', 'lilya qwew', 'dcf', 'qwey')
# 'kids tennis', '16:00', '17:30', 'Tuesday', 'lilya qwew', 'dcf', 'qwey'
# g.check_student_in_group('kids tennis', '19:30', '20:30', 'Thursday', 'lilya qwew', 'dcf', 'qwey')
# g.insert_student_to_group('5', '1')
# g.delete_student_from_group('4','1')
# g.get_students_by_group_id('1')
# g.get_all_groupsstudents()
# g.get_student_names_by_group_id('1')
# g.get_student_name_by_group_name("swimming")