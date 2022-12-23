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
