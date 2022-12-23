import random
from Data.AccountRepository import AccountRepository
from Model.Transaction import Transaction


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
                digit = str(random.randint(1, 9))
            else:
                digit = str(random.randint(0, 9))
            accountNumber = accountNumber + digit

        self.accountNumber = accountNumber

    def makeTransaction(self, toID, amount):
        fromID = self.accountNumber
        new_transaction = Transaction(fromID, toID, amount, 1)
        repo = AccountRepository()
        repo.updateBalance(-amount, fromID)
        repo.updateBalance(amount, toID)
        self.transactionList.append(new_transaction)
