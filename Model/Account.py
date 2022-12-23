from Data.AccountRepository import AccountRepository as accounts


class Account:

    def __init__(self):
        pass

    def createAccount(self, accountName, currencyType, userId):
        AccountTable = accounts()
        accounts.createAccount(AccountTable, accountName, currencyType, userId)

    def listAccounts(self, userId):
        return accounts.getAccountsOfUser(accounts(), userId)
