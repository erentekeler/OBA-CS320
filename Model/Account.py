import random
from Data.AccountRepository import AccountRepository
from Model.Transaction import Transaction


class Account:

    def __init__(self):
        pass

    def makeTransaction(self, toID, amount):
        fromID = self.accountNumber
        new_transaction = Transaction(fromID, toID, amount, 1)
        repo = AccountRepository()
        repo.updateBalance(-amount, fromID)
        repo.updateBalance(amount, toID)
        self.transactionList.append(new_transaction)
