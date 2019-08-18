import sys

import pymysql
import pymysql.cursors
import dbconfig

# The four main database operations CRUD - Create. Read. Update. Delete


class DBHelper:

    #   --- CREATE --- Create and Insert New Data

    def connects(self, database="crimemap"):
        try:
            conn = pymysql.connect(host='localhost',
                                   user=dbconfig.db_user,
                                   password=dbconfig.db_password,
                                   db=database,
                                   charset='utf8mb4',
                                   cursorclass=pymysql.cursors.DictCursor)
        except Exception as e:
            print(e)
        return conn
    # --- READ --- Read Exsiting Data

    def get_all_inputs(self):
        connection = self.connects()
        try:
            query = "SELECT description FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
            return cursor.fetchall()
        finally:
            connection.close()

    # --- UPDATE --- Modify Existing Data

    def add_input(self, data):
        connection = self.connects()
        try:
            # The following introduces a deliberate security flaw. See section on SQL injecton below
            query = "INSERT INTO crimes (description) VALUES (%s);"
            with connection.cursor() as cursor:
                cursor.execute(query, data)
                connection.commit()
        finally:
            connection.close()

    # --- DELETE --- Delete Exsising Data

    def clear_all(self):
        connection = self.connects()
        try:
            query = "DELETE FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()

    def add_crime(self, category, date, latitude, longitude, description):
        connection = self.connects()
        try:
            query = "INSERT INTO crimes(category, date, latitude,
                                        longitude, description) \
                VALUES ( % s, % s, % s, % s, % s)"
            with connection.cursor() as cursor:
                cursor.execute(
                    query, (category, date, latitude, longitude, description))
                connection.commit()
        except Exception as e:
            print(e)
        finally:
            connection.close()
