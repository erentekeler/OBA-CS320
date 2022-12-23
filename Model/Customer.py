from Model.Account import Account


class Customer:

    def __init__(self, name, surname, tckn, password, accountList):
        self.name = name
        self.surname = surname
        self.tckn = tckn
        self.password = password
        self.accountList = accountList

    def createAccount(self, accountName, currencyType):
        new_account = Account(accountName, currencyType)
        self.accountList.append(new_account)

    def updateDatabase(self):
        print("Customer.updateDatabase()")
