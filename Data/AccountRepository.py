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
                    query = "INSERT INTO Account (AccountName, CurrencyType, Balance, UserId) VALUES (" + "\'" + str(accountName) + "\'" + " , " + "\'" + str(currencyType) + "\'" +" , " +  str(0) + " , " + str(userId) +")"
                    tempResult = query
                    continue
            result = tempResult
            if tempResult == query:
                result = self.connector.executeQuery(query,True)
                return True
            else:
                return False
        else:
            query = "INSERT INTO Account (AccountName, CurrencyType, Balance, UserId) VALUES (" + "\'" + str(accountName) + "\'" + " , " + "\'" + str(currencyType) + "\'" +" , " +  str(0) + " , " + str(userId) +")"
            result = self.connector.executeQuery(query, True)
            return True

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

    #ok
    def updateBalance(self, amount, accountId):
        query = "UPDATE account SET Balance = " + str(amount) + " WHERE AccountId = " + str(accountId)
        result = self.connector.executeQuery(query, True)

    #ok
    def getAccountBalanceFromAccountName(self, accountName, userId):
        query = "select Balance from Account where AccountName = " +  "\'" + str(accountName) + "\'" + " and UserId = " + str(userId)
        result = self.connector.executeQuery(query)
        return result

    def getCurrencyFromAccountName(self, accountName, userId):
        query = "select CurrencyType from Account where AccountName = " + "\'" + str(accountName) + "\'" + " and UserId = " + str(userId)
        result = self.connector.executeQuery(query)
        return result


    def getAccountBalanceAccountId(self,accountId):
        query = "select Balance from Account where AccountId = " + str(accountId)
        result = self.connector.executeQuery(query)
        return result

    def getAccountIdFromAccountName(self,accountName, userId):
        query = "select AccountId from Account where AccountName = " + "\'" + str(accountName) + "\'" + " and UserId = " + str(userId)
        result = self.connector.executeQuery(query)
        return result

    def getFullNameFromAccountId(self, accountId):
        query = "select u.FirstName, u.LastName from account as a, user as u where u.UserId = a.UserId and a.AccountId = "+ str(accountId)
        result = self.connector.executeQuery(query)
        return result

    def getAccountNameFromCurrencyType(self, userId, currencyType):
        query = "select AccountName from account as a where userID = " + str(userId) + " and currencyType= " + "\'" + str(currencyType) + "\'"
        result = self.connector.executeQuery(query)
        if(result is None): return None
        else: return result


    def returnMultipleRowAsList(self, rows):
        lst = []
        for row in rows:
            for data in row:
                lst.append(data)
        return lst
