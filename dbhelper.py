import pymysql
import dbconfig

# The four main database operations CRUD - Create. Read. Update. Delete


class DBHelper:

    #   --- CREATE --- Create and Insert New Data

    def connect(self, database="crimemap"):
        return pymysql.connect(host='localhost',
                               user=dbconfig.db_user,
                               password=dbconfig.db_password,
                               db=database)

    # --- READ --- Read Exsiting Data

    def get_all_inputs(self):
        connection = self.connect()
        try:
            query = "SELECT description FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
            return cursor.fetchall()
        finally:
            connection.close()

    # --- UPDATE --- Modify Existing Data

    def add_input(self, data):
        connection = self.connect()
        try:
            # The following introduces a deliberate security flaw. See section on SQL injecton below
            query = "INSERT INTO crimes (description) VALUES ('{}');".format(
                data)
            with connect.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()

    # --- DELETE --- Delete Exsising Data

    def clear_all(self):
        connection = self.connect()
        try:
            query = "DELETE FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
                cursor.commit
        finally:
            connection.close()
