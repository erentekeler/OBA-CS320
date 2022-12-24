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
        query = f'INSERT INTO Transaction (SenderAccountId, RecieverAccountId, TransactionDate, Amount, CurrencyType)' \
                f' VALUES (\'{senderAccountId}\', \'{receiverAccountId}\', \'{now}\', \'{amount}\', \'{currencyType}\')'
        print("laaaaan")
        result = self.connector.executeQuery(query, True)
        print(result)
