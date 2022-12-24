import sys
import os
os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.insert(1, os.getcwd())
from Data import MySqlConnector as ml
from datetime import datetime
from Data import AccountRepository as ar

class TransactionRepository:

    def __init__(self):
        self.connector = ml.MySqlConnector()
        self.AR = ar.AccountRepository()

    def getReceiverAccountTransactions(self, accountId):
        query = "select * from Transaction where ReceiverAccountId = " + str(accountId)
        result = self.connector.executeQuery(query)
        return result

    def getSenderAccountTransactions(self, accountId):
        query = "select * from Transaction where SenderAccountId = " + str(accountId)
        result = self.connector.executeQuery(query)
        return result

    def createTransaction(self, senderAccountId, receiverAccountId, amount, currencyType):
        now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        query = f'INSERT INTO Transaction (SenderAccountId, ReceiverAccountId, TransactionDate, Amount, CurrencyType)' \
                f' VALUES (\'{senderAccountId}\', \'{receiverAccountId}\', \'{now}\', \'{amount}\', \'{currencyType}\')'
        result = self.connector.executeQuery(query, True)

    def getReceivedTransactions(self, userId):
        query = "select a.accountName, t.Amount, t.CurrencyType, t.TransactionDate from Account as a, transaction as t where a.UserId = " + str(userId) + " and t.ReceiverAccountId = a.AccountId";
        result = self.connector.fetch_as_all(query)
        return result

    def getSentTransactions(self, userId):
        query = "select a.accountName, t.Amount, t.CurrencyType, t.TransactionDate from Account as a, transaction as t where a.UserId = " + str(userId) + " and t.SenderAccountId = a.AccountId"
        result = self.connector.fetch_as_all(query)
        return result
