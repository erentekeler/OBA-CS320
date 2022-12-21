from MySqlConnector import MySqlConnector
from datetime import datetime
from AccountRepository import AccountRepository

class TransactionRepository:

    def __init__(self):
        self.connector = MySqlConnector()

    def getUserTransactions(self, userId):
        query = "select * from Transaction where UserId = " + str(userId)
        result = self.connector.executeQuery(query)
        return result

    #balance account create edildiğinde 0 olduğu için 0 yazdım.
    def createTransaction(self, senderAccountId, recieverAccountId, amount):
        now = datetime.now()
        currencyType = AccountRepository.getAccount(senderAccountId)[2]
        query =  f'INSERT INTO Transaction (SenderAccountId, RecieverAccountId, TransactionDate, Amount, CurrencyType) VALUES (\'{senderAccountId}\', \'{recieverAccountId}\', \'{now}\', \'{amount}\', \'{currencyType}\')'
        print(query)
        result = self.connector.executeQuery(query, True)
        print(result)
