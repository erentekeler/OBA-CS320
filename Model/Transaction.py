from Data.TransactionRepository import TransactionRepository as transactions
from Data.AccountRepository import AccountRepository as accounts


class Transaction:

    def __init__(self):
        pass

    def makeTransaction(self, fromID, toID, amount):
        amount = float(amount.strip())
        TransactionTable = transactions()
        AccountTable = accounts()
        senderType = accounts.getAccountFromAccountId(AccountTable, fromID)[2]
        receiverType = accounts.getAccountFromAccountId(AccountTable, toID)[2]
        if senderType == receiverType:
            transactions.createTransaction(TransactionTable, fromID, toID, amount)
            currBalanceSender = float(accounts.getAccountBalanceAccountId(accounts(), fromID))
            currBalanceReceiver = float(accounts.getAccountBalanceAccountId(accounts(), toID))
            accounts.updateBalance(AccountTable, currBalanceSender - amount, fromID)
            accounts.updateBalance(AccountTable, currBalanceReceiver + amount, toID)

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
