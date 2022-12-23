from Data.TransactionRepository import TransactionRepository as transactions


class Transaction:

    def __init__(self):
        pass

    def makeTransaction(self, fromID, toID, amount):
        TransactionTable = transactions()
        transactions.createTransaction(TransactionTable, fromID, toID, amount)

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
