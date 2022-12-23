from Model.Account import Account


class Customer:

    def __init__(self):
        pass

    def createAccount(self, accountName, currencyType):
        new_account = Account(accountName, currencyType)
        self.accountList.append(new_account)

    def updateDatabase(self):
        print("Customer.updateDatabase()")
