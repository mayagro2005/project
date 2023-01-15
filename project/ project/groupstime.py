import sqlite3
import hashlib

class groupstime(object):
    def __init__(self, tablename = "groupstime", timeId = "timeId", groupId = "groupId", startH = "startH", endH = "endH", lessonDay = "lessonDay"):
        self.__tablename = tablename
        self.__timeId = timeId
        self.__groupId = groupId
        self.__startH = startH
        self.__endH = endH
        self.__lessonDay = lessonDay


        conn = sqlite3.connect('test.db')
        print ("Opened database successfully")
        str = "CREATE TABLE IF NOT EXISTS " + self.__tablename + "(" + self.__timeId + " " + "INTEGER PRIMARY KEY AUTOINCREMENT ,"
        str += " " + self.__groupId + " TEXT    NOT NULL ,"
        str += " " + self.__startH + " TEXT    NOT NULL, "
        str += " " + self.__endH + " TEXT    NOT NULL, "
        str += " " + self.__lessonDay + " TEXT    NOT NULL) "
        conn.execute(str)
        print("Table created successfully");
        conn.commit()
        conn.close()
    def get_table_name(self):
        return self.__tablename

    def get_all_groups_times(self):
        conn = sqlite3.connect('test.db')
        print("Opened database successfully")
        str_select = "SELECT * from " + self.__tablename
        cursor = conn.execute(str_select)
        rows = cursor.fetchall()
        groups_times = []
        for row in rows:
            groups_times.append({
                "timeId": row[0],
                "groupId": row[1],
                "startH": row[2],
                "endH": row[3],
                "lessonDay": row[4]
            })
        print(groups_times)
        return groups_times


    def insert_group_time(self, groupId, startH, endH, lessonDay):
        conn = sqlite3.connect('test.db')
        print("Opened database successfully")
        str_check = f"SELECT * from {self.__tablename} where '{groupId}' = {self.__groupId} and " \
                    f"'{startH}' = {self.__startH} and '{endH}' = {self.__endH} and '{lessonDay}' = {self.__lessonDay}"
        print(str_check)
        cursor = conn.execute(str_check)
        row = cursor.fetchall()
        if row:
            print("Group time already exists")
            return False
        else:
            try:
                str_insert = f"INSERT INTO {self.__tablename} ({self.__groupId}, {self.__startH}, {self.__endH}, {self.__lessonDay})" \
                             f" VALUES ('{groupId}', '{startH}', '{endH}', '{lessonDay}');"
                print(str_insert)
                conn.execute(str_insert)
                conn.commit()
                conn.close()
                print("Record created successfully");
                return True
            except:
                print("Failed to insert group time")
                return False

    def delete_group_time(self, groupId, startH, endH, lessonDay):
        conn = sqlite3.connect('test.db')
        print("Opened database successfully")
        str_check = f"SELECT * from {self.__tablename} where {self.__groupId} = {groupId} and " \
                    f"{self.__startH} = {startH} and {self.__endH} = {endH} and {self.__lessonDay} = {lessonDay}"
        cursor = conn.execute(str_check)
        row = cursor.fetchall()
        if row:
            try:
                str_delete = f"DELETE from {self.__tablename} where {self.__groupId} = {groupId} and " \
                             f"{self.__startH} = {startH} and {self.__endH} = {endH} and {self.__lessonDay} = {lessonDay}"
                conn.execute(str_delete)
                conn.commit()
                conn.close()
                print("Record deleted successfully")
                return "Success"
            except:
                return "Failed to delete record"
        else:
            return "Record not found"



    def get_group_name_by_time_id(self, timeId):
        conn = sqlite3.connect('test.db')
        str_select = f"SELECT nameofgroup FROM groups INNER JOIN {self.__tablename} ON groups.groupId = {self.__tablename}.groupId WHERE {self.__timeId} = '{timeId}'"
        cursor = conn.execute(str_select)
        row = cursor.fetchone()
        if row:
            print(row[0])
            return row[0]
        else:
            print("there is no group")
            return None

    def update_group_time(self, groupId, startH, endH, lessonDay, groupId1, startH1, endH1, lessonDay1):
        conn = sqlite3.connect('test.db')
        str_update = f"UPDATE {self.__tablename} SET {self.__groupId} = '{groupId}', {self.__startH} = '{startH}', {self.__endH} = '{endH}', {self.__lessonDay} = '{lessonDay}' WHERE {self.__groupId} = '{groupId1}' AND {self.__startH} = '{startH1}' AND {self.__endH} = '{endH1}' AND {self.__lessonDay} = '{lessonDay1}'"
        try:
            print(str_update)
            conn.execute(str_update)
            conn.commit()
            print("Record updated successfully")
            return True
        except:
            return False

    def get_group_by_day(self, lessonDay):
        conn = sqlite3.connect('test.db')
        str_select = f"SELECT groups.nameofgroup, groups.groupId, {self.__tablename}.startH, {self.__tablename}.endH, {self.__tablename}.lessonDay FROM groups INNER JOIN {self.__tablename} ON groups.groupId = {self.__tablename}.groupId WHERE {self.__tablename}.lessonDay = '{lessonDay}'"
        cursor = conn.execute(str_select)
        rows = cursor.fetchall()
        if rows:
            print(rows)
            return rows
        else:
            return None


g = groupstime()
# g.insert_group_time('2', '17:00', '18:30', "sunday")
<<<<<<< HEAD
g.get_all_groups_times()
=======
# g.get_all_groups_times()
>>>>>>> origin/main
# g.get_group_name_by_time_id('1')
# g.update_group_time('2', '18:00', '19:00', "monday", '2', '17:00', '18:30', "sunday")
# g.get_group_by_day("monday")

