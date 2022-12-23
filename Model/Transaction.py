from Data.TransactionRepository import TransactionRepository as transactions
from Data.AccountRepository import AccountRepository as accounts


class Transaction:

    def __init__(self):
        pass

    def makeTransaction(self, fromID, toID, amount):
        TransactionTable = transactions()
        AccountTable = accounts()
        senderType = accounts.getAccountFromIBAN(AccountTable, fromID)[2]
        receiverType = accounts.getAccountFromIBAN(AccountTable, toID)[2]
        if senderType == receiverType:
            transactions.createTransaction(TransactionTable, fromID, toID, amount)
            return True
        else:
            return False

    def filterTransactionsByType(self, accountId, keyword):
        TransactionTable = transactions()

        if keyword == "Received":
            return transactions.getReceiverAccountTransactions(TransactionTable, accountId)
        elif keyword == "Sent":
            return transactions.getSenderAccountTransactions(TransactionTable, accountId)

    def filterTransactionsByAmount(self, accountId, amount, keyword):
        TransactionTable = transactions()

        allTransactions = transactions.getSenderAccountTransactions(TransactionTable, accountId) + \
            transactions.getReceiverAccountTransactions(TransactionTable, accountId)

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
