import sqlite3
import hashlib
from dbteachers import teachers
from groups import groups
class groupstime(object):
    def __init__(self, tablename = "groupstime", timeId = "timeId", groupId = "groupId", startH = "startH", endH = "endH", lessonDay = "lessonDay"):
        self.__tablename = tablename
        self.__timeId = timeId
        self.__groupId = groupId
        self.__startH = startH
        self.__endH = endH
        self.__lessonDay = lessonDay
        self.teachers = teachers



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
                # "timeId": row[0],
                "groupId": row[1],
                "startH": row[2],
                "endH": row[3],
                "lessonDay": row[4]
            })
        arr_groups_times = [[group_time["groupId"], group_time["startH"], group_time["endH"], group_time["lessonDay"]]
                            for group_time in groups_times]
        print(arr_groups_times)
        return arr_groups_times

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
            return "exist"
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
        try:
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM {} WHERE {} = ? AND {} = ? AND {} = ? AND {} = ?".format(self.__tablename, self.__groupId, self.__startH, self.__endH, self.__lessonDay), (groupId, startH, endH, lessonDay))
            row = cursor.fetchone()
            if row:
                cursor.execute("DELETE FROM {} WHERE {} = ? AND {} = ? AND {} = ? AND {} = ?".format(self.__tablename, self.__groupId, self.__startH, self.__endH, self.__lessonDay), (groupId, startH, endH, lessonDay))
                conn.commit()
                print("Success")
                return "Success"
            else:
                print("not found")
                return "not found"
        except:
            return "Failed to delete record"


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

    def get_details_by_group_id(self, groupId):
        try:
            conn = sqlite3.connect('test.db')
            str_select = f"SELECT startH, endH, lessonDay FROM {self.__tablename} WHERE {self.__groupId} = '{groupId}'"
            cursor = conn.execute(str_select)
            rows = cursor.fetchall()
            if rows:
                results = []
                for row in rows:
                    results.append({
                        "startH": row[0],
                        "endH": row[1],
                        "lessonDay": row[2]})
                arr_groups_times = [
                    [row["startH"], row["endH"], row["lessonDay"]]
                    for row in results]
                print(arr_groups_times)
                return arr_groups_times
            else:
                print("there is no group")
                return "there is no group"
        except:
            print("error")
            return "error"

    def delete_group_by_timeid(self,timeId):
        try:
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM groupstime WHERE timeId = ?", (timeId,))
            row = cursor.fetchone()
            if row:
                cursor.execute("DELETE FROM groupstime WHERE timeId = ?", (timeId,))
                conn.commit()
                print("Success")
                return "Success"
            else:
                print("not found")
                return "not found"
        except:
            return "Failed to delete record"

    def update_group_time(self, groupId, startH, endH, lessonDay, groupId1, startH1, endH1, lessonDay1):
        try:
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            check_query = f"SELECT * FROM {self.__tablename} WHERE {self.__groupId} = '{groupId1}' AND {self.__startH} = '{startH1}' AND {self.__endH} = '{endH1}' AND {self.__lessonDay} = '{lessonDay1}'"
            cursor.execute(check_query)
            result = cursor.fetchone()
            if result:
                str_update = f"UPDATE {self.__tablename} SET {self.__groupId} = '{groupId}', {self.__startH} = '{startH}', {self.__endH} = '{endH}', {self.__lessonDay} = '{lessonDay}' WHERE {self.__groupId} = '{groupId1}' AND {self.__startH} = '{startH1}' AND {self.__endH} = '{endH1}' AND {self.__lessonDay} = '{lessonDay1}'"
                conn.execute(str_update)
                conn.commit()
                print("Record updated successfully")
                return True
            else:
                print("Record does not exist")
                return "Record does not exist"
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
# g.delete_group_by_timeid(5)
# g.delete_group_time('8',"18:00","19:00","thursday")
# g.insert_group_time('2', '17:00', '18:30', "sunday")
# g.insert_group_time('1','18:00','20:00',"tuesday")
# g.insert_group_time('7','18:30','19:30',"tuesday")
# g.get_all_groups_times()
# g.get_all_groups_times()
arr = g.get_details_by_group_id('7')
print(arr[0][0])
# g.get_all_groups_times()
# g.get_group_name_by_time_id('1')
# g.update_group_time('2', '18:30', '19:30', "Monday", '2','18:00','19:00',"monday")
# g.get_group_by_day("monday")


