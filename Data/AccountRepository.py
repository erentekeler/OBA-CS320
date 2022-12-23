import os, sys
os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.insert(1, os.getcwd())
from Data import MySqlConnector as ml
import numpy as np


class AccountRepository:

    def __init__(self):
        self.connector = ml.MySqlConnector()

    def getAccount(self, ID):
        query = "select * from Account where AccountId = " + str(ID)
        result = self.connector.executeQuery(query)
        return result

    # balance account create edildiğinde 0 olduğu için 0 yazdım.
    def createAccount(self, accountName, currencyType, userId):
        tempResult = ""
        query = ""
        if len(self.getAccountNamesOfUser(userId)) > 0:
            for name in self.getAccountNamesOfUser(userId):
                if accountName == name:
                    tempResult = "You already have an account with the same name."
                    break
                else:
                    query = f'INSERT INTO Account (AccountName, CurrencyType, Balance, UserId) VALUES (\'{accountName}\', \'{currencyType}\', \'{0}\', \'{userId}\')'
                    tempResult = query
                    continue
            result = tempResult
            if tempResult == query:
                result = self.connector.executeQuery(query)
        else:
            query = f'INSERT INTO Account (AccountName, CurrencyType, Balance, UserId) VALUES (\'{accountName}\', \'{currencyType}\', \'{0}\', \'{userId}\')'
            result = self.connector.executeQuery(query, True)
        print(result)

    def getAccountsOfUser(self, userId):
        query = "select * from Account where UserId = " + str(userId)
        result = self.connector.executeQuery(query)
        return result

    def getAccountNamesOfUser(self, userId):
        query = "SELECT AccountName from Account WHERE UserId = " + str(userId)
        result = self.connector.fetch_as_all(query)
        return self.returnMultipleRowAsList(result)

    def getAccountFromAccountId(self, accountId):
        query = "select * from Account where AccountId = " + str(accountId)
        result = self.connector.executeQuery(query)
        return result

    def updateBalance(self, amount, accountId):
        query = "UPDATE account SET Balance = " + str(amount) + " WHERE AccountId = " + str(accountId)
        result = self.connector.executeQuery(query, True)
        return result

    def getAccountBalanceFromAccountName(self, accountName, userId):
        query = "select Balance from Account where AccountName = " + str(accountName) + "and UserId= " + str(userId)
        result = self.connector.executeQuery(query)
        return result

    def returnMultipleRowAsList(self, rows):
        lst = []
        for row in rows:
            for data in row:
                lst.append(data)
        return lst

    # def countNumberOfUserAccounts(self, userId):
    #     query = "SELECT Count(*) FROM Account WHERE UserId = " + str(userId)
    #     result = self.connector.executeQuery(query)[0]
    #     return result

A = AccountRepository()
# A.getAccountNamesOfUser(3)
# A.createAccount("Eren", "TL", "1234567890", 1)
# A.updateBalance(350, "1234567890")
b = A.getAccountNamesOfUser(4)[0]
c = A.getAccountBalanceFromAccountName("TL hesabım" ,4)
print(c)