import sys
import os
os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.insert(1,os.getcwd())
from Data import AccountRepository as acc


class Account:

    def __init__(self):
        pass

    def createAccount(self, accountName, currencyType, userId):
        AccountTable = acc.AccountRepository()
        return AccountTable.createAccount(accountName, currencyType, userId)

    def listAccounts(self, userId):
        AccountTable = acc.AccountRepository()
        return acc.getAccountsOfUser(userId)

    def getUserFullNameFromAccountId(self, accountId):
        AccountTable = acc.AccountRepository()
        temp = AccountTable.getFullNameFromAccountId(accountId)
        if(temp is not None): return temp[0] + " " + temp[1]
        else: return False
