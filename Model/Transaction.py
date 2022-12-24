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

    def makeTransaction(self, accountName, userId, toAccountID, amount):
        amount = float(amount.strip())
        senderType = self.AccountTable.getCurrencyFromAccountName(accountName, userId)[0]
        receiverType = self.AccountTable.getAccountFromAccountId(toAccountID)[2]
        if senderType == receiverType:
            fromAccountId = self.AccountTable.getAccountIdFromAccountName(accountName, userId)[0]
            self.TransactionTable.createTransaction(fromAccountId, toAccountID, amount, receiverType)
            currBalanceSender = float(self.AccountTable.getAccountBalanceAccountId(fromAccountId)[0])
            currBalanceReceiver = float(self.AccountTable.getAccountBalanceAccountId(toAccountID)[0])
            self.AccountTable.updateBalance(currBalanceSender - amount, fromAccountId)
            self.AccountTable.updateBalance(currBalanceReceiver + amount, toAccountID)
            return True
        else: return False

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
