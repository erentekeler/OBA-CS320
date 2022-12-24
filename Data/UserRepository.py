import sys
import os
os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.insert(1,os.getcwd())
from Data import MySqlConnector as sql


class UserRepository:

    def __init__(self):
        self.connector = sql.MySqlConnector()

    def getUser(self, id):
        query = "select * from User where UserId = " + str(id)
        result = self.connector.executeQuery(query)
        return result

    def getUserPassword(self, identityNumber):
        query = "select Password from User where IdentityNumber = " + str(identityNumber)
        result = self.connector.executeQuery(query)
        return result[0]

    def createUser(self, firstName, lastName, password, identityNumber):
        query = f'INSERT INTO User (FirstName, LastName, Password, IdentityNumber) VALUES (\'{firstName}\', \'{lastName}\', \'{password}\', \'{identityNumber}\')'
        result = self.connector.executeQuery(query, True)

    def getLoginUser(self, identityNumber, password):
        query = f'select * from User where IdentityNumber = \'{identityNumber}\' AND Password = \'{password}\''
        result = self.connector.executeQuery(query)
        return result

    def getUserIdFromIdentityNo(self, identityNumber):
        query = f'select UserId from User where IdentityNumber = \'{identityNumber}\''
        result = self.connector.executeQuery(query)
        return result[0]

    def getUserIdFromIdentityNoV2(self, identityNumber):
        query = f'select UserId from User where IdentityNumber = \'{identityNumber}\''
        result = self.connector.executeQuery(query)
        return result



