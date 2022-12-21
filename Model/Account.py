import random

class Account:

    def __init__(self, accountName, currencyType):
        self.balance = 0
        self.accountName = accountName
        self.currencyType = currencyType
        self.transactionList = []

        accountNumber = ""
        IBAN = "TR44"

        for i in range(8):
            if i == 1:
                digit = str(randint(1,9))
            else:
                digit = str(randint(0,9))
            accountNumber = accountNumber + digit


        for i in range(22):
            IBAN = IBAN + str(randint(0,9))

        self.accountNumber = accountNumber
        self.IBAN = IBAN

    def makeTransaction(self, toIBAN, amount):
        new_transaction = Transaction(fromIBAN, toIBAN, amount)

        for account in self.accountList:
            if account.IBAN == fromIBAN:
                account.transactionList.append = new_transaction

        receiver = findAccountFromIBAN(toIBAN)

    def findAccountFromIBAN(self, IBAN) -> Account:
        print("search database and find the related account")

    def updateDatabase(self):
        print("Account.updateDatabase()")