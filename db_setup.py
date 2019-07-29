import pymysql
import dbconfig

connection = pymysql.connect(host='localhost',
                             user=dbconfig.db_user,
                             password=dbconfig.db_password)
try:
    with connection.cursor() as cursor:
        sql = "CREATE DATABASE IF NOT EXSISTS crimemap"
        cursor.execute(sql)
        sql = """ CREATE TABLE IF NOT EXSISTS crimemap.create(
        id int NOT NULL AUTO_INCREMENT,
        latitude FLOAT(10, 6),
        longitude FLOAT(10, 6),
        date DATETIME,
        category VARCHAR(50),
        description VARCHAR(1000),
        update_at TIMESTAMP,
        primary key (id)
        )"""
        cursor.execute(sql)
        connection.commit()
finally:
    connection.close()
