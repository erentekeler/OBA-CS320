import random
from Data.AccountRepository import AccountRepository as accounts
from Model.Transaction import Transaction


class Account:

    def __init__(self):
        pass

    def createAccount(self, accountName, currencyType, userId):
        AccountTable = accounts()
        accounts.createAccount(AccountTable, accountName, currencyType, userId)

    def listAccounts(self, userId):
        return accounts.getAccountsOfUser(accounts(), userId)
