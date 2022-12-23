import pymysql

class MySqlConnector:
    def __init__(self):
        self.connection = pymysql.connect(host="localhost", user="root", password="CS320", database="obadb")

    #eğer select komutu varsa default commit false olduğu için parametreyi çağırmaya gerek yok.
    #diğer komutlar için commit parametresi true olarak çağrılmalı.
    def executeQuery(self, query, commit = False):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            if commit:
                self.connection.commit()
            return cursor.fetchone()
        except pymysql.Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            cursor.close()
            print("MySQL connection is closed")

    def fetch_as_all(self, select_query):
    #'''Execute a select query and return the outcome as a dict.'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(select_query)
            rows = cursor.fetchall()
            return rows
        except:
            msg = 'ERROR'
            print(msg)
        finally:
            cursor.close()
            print("MySQL connection is closed")