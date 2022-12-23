import sys
import os
os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.insert(1,os.getcwd())
from Data.AccountRepository import AccountRepository as acc


class Account:

    def __init__(self):
        pass

    def createAccount(self, accountName, currencyType, userId):
        AccountTable = acc.createAccount()
        return AccountTable.createAccount(accountName, currencyType, userId)

    def listAccounts(self, userId):
        return accounts.getAccountsOfUser(accounts(), userId)
