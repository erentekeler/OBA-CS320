import sys
import os
os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.insert(1,os.getcwd())
from Data import UserRepository as users


class Customer:

    def __init__(self):
        pass

    def createUser(self, firstName, lastName, password, identityNumber):
        UserTable = users.UserRepository()
        UserTable.createUser(firstName, lastName, password, identityNumber)

    def loginCheck(self, identityNumber, password) -> bool:
        UserTable = users.UserRepository()
        if(identityNumber == "" or password == ""): return False
        else: return UserTable.getUserIdFromIdentityNo(identityNumber) is not None and UserTable.getUserPassword(identityNumber) is not None and password == UserTable.getUserPassword(identityNumber)


    def registerCheck(self, identityNumber):
        UserTable = users.UserRepository()
        if (identityNumber == ""): return False
        else: return UserTable.getUserIdFromIdentityNo(identityNumber) is None

