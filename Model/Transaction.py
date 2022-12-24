import sys
import os
os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.insert(1, os.getcwd())
from Data import TransactionRepository as tr
from Data import AccountRepository as ac


class Transaction:

    def __init__(self):
        self.TransactionTable = tr.TransactionRepository()
        self.AccountTable = ac.AccountRepository()
        pass

    def makeTransaction(self, fromID, toID, amount):
        amount = float(amount.strip())
        senderType = self.AccountTable.getAccountFromAccountId(fromID)[2]
        receiverType = self.AccountTable.getAccountFromAccountId(toID)[2]
        if senderType == receiverType:
            self.TransactionTable.createTransaction(fromID, toID, amount)
            currBalanceSender = float(self.AccountTable.getAccountBalanceAccountId(fromID))
            currBalanceReceiver = float(self.AccountTable.getAccountBalanceAccountId(toID))
            self.AccountTable.updateBalance(currBalanceSender - amount, fromID)
            self.AccountTable.updateBalance(currBalanceReceiver + amount, toID)

    def filterTransactionsByType(self, accountId, keyword):

        if keyword == "Received":
            return self.TransactionTable.getReceiverAccountTransactions(accountId)
        elif keyword == "Sent":
            return self.TransactionTable.getSenderAccountTransactions(accountId)

    def filterTransactionsByAmount(self, accountId, amount, keyword):

        allTransactions = self.TransactionTable.getSenderAccountTransactions( accountId) + \
            self.TransactionTable.getReceiverAccountTransactions(accountId)

        filteredTransactions = []

        if keyword == "Larger":
            for transaction in allTransactions:
                if transaction[4] >= amount:
                    filteredTransactions.append(transaction)
        elif keyword == "Less Than":
            for transaction in allTransactions:
                if transaction[4] <= amount:
                    filteredTransactions.append(transaction)

        return filteredTransactions
