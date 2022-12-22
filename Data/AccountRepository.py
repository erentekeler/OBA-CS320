from MySqlConnector import MySqlConnector

class AccountRepository:

    def __init__(self):
        self.connector = MySqlConnector()

    def getAccount(self, id):
        query = "select * from Account where AccountId = " + str(id)
        result = self.connector.executeQuery(query)
        return result

    #balance account create edildiğinde 0 olduğu için 0 yazdım.
    def createAccount(self, accountName, currencyType, accountNumber, userId):
        query =  f'INSERT INTO Account (AccountName, CurrencyType, AccountNumber, Balance, UserId) VALUES (\'{accountName}\', \'{currencyType}\', \'{accountNumber}\', \'{0}\', \'{userId}\')'
        print(query)
        result = self.connector.executeQuery(query, True)
        print(result)

    def getAccountsOfUser(self, userId):
        query = "select * from Account where UserId = " + str(userId)
        result = self.connector.executeQuery(query)
        return result
    
    def getAccountFromIBAN(self, accountNumber):
        query = "select * from Account where AccountNumber = " + str(accountNumber)
        result = self.connector.executeQuery(query)
        return result