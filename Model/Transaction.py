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

    def filterTransactions(self, userId, key):
        if key == 1:
            received = self.TransactionTable.getReceivedTransactions(userId)
            if(received is not None):
                received = list(received)
                received.reverse()
                received = received[0:5]
                return received
            else: return []
        elif key == 2:
            sent = self.TransactionTable.getSentTransactions(userId)
            if (sent is not None):
                sent = list(sent)
                sent.reverse()
                sent = sent[0:5]
                return sent
            else: return []

