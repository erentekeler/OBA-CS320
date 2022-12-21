from pickle import FALSE
import pymysql

class MySqlConnector:
    def __init__(self):
        self.connection = pymysql.connect(host="localhost", user="root", password="irem123.", database="obadb")

    #eğer select komutu varsa default commit false olduğu için parametreyi çağırmaya gerek yok.
    #diğer komutlar için commit parametresi true olarak çağrılmalı.
    def executeQuery(self, query, commit = False):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            if commit:
                self.connection.commit()
            return cursor.fetchone(),
        except pymysql.Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            cursor.close()
            print("MySQL connection is closed")
