from MySqlConnector import MySqlConnector
from datetime import datetime
from AccountRepository import AccountRepository

class TransactionRepository:

    def __init__(self):
        self.connector = MySqlConnector()


    def getReceiverAccountTransactions(self, accountId):
        query = "select * from Transaction where ReceiverAccountId = " + str(accountId)
        result = self.connector.executeQuery(query)
        return result

    def getSenderAccountTransactions(self, accountId):
        query = "select * from Transaction where SenderAccountId = " + str(accountId)
        result = self.connector.executeQuery(query)
        return result

    #balance account create edildiğinde 0 olduğu için 0 yazdım.
    def createTransaction(self, senderAccountId, receiverAccountId, amount):
        now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        currencyType = AccountRepository.getAccount(AccountRepository(), senderAccountId)[2]
        query = f'INSERT INTO Transaction (SenderAccountId, RecieverAccountId, TransactionDate, Amount, CurrencyType)' \
                f' VALUES (\'{senderAccountId}\', \'{receiverAccountId}\', \'{now}\', \'{amount}\', \'{currencyType}\')'
        print(query)
        result = self.connector.executeQuery(query, True)
        print(result)
