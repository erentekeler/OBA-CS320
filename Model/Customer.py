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
        else: return UserTable.getUserIdFromIdentityNoV2(identityNumber) is not None and UserTable.getUserPassword(identityNumber) is not None and password == UserTable.getUserPassword(identityNumber)


    def registerCheck(self, identityNumber):
        UserTable = users.UserRepository()
        print(len(str(identityNumber)))
        if (identityNumber == ""): return False
        elif(len(str(identityNumber)) != 11):return str(7)
        elif(UserTable.getUserIdFromIdentityNoV2(identityNumber) is not None): return str(8)
        else: return UserTable.getUserIdFromIdentityNoV2(identityNumber) is None

