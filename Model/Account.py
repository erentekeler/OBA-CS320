import sys
import os
os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.insert(1,os.getcwd())
from Data import AccountRepository as acc
import requests


class Account:

    def __init__(self):
        self.AccountTable = acc.AccountRepository()
        pass

    def createAccount(self, accountName, currencyType, userId):
        AccountTable = acc.AccountRepository()
        return AccountTable.createAccount(accountName, currencyType, userId)

    def listAccounts(self, userId):
        AccountTable = acc.AccountRepository()
        return acc.getAccountsOfUser(userId)

    def getUserFullNameFromAccountId(self, accountId):
        AccountTable = acc.AccountRepository()
        temp = AccountTable.getFullNameFromAccountId(accountId)
        if(temp is not None): return temp[0] + " " + temp[1]
        else: return False

    def getCurrencyData(self,fromCurrencyType):
        url = 'https://v6.exchangerate-api.com/v6/c6c7034ecf734c77fc0c296c/latest/' + str(fromCurrencyType)
        response = requests.get(url)
        data = response.json()
        return data["conversion_rates"]

    def exchangeCurrency(self, userId, fromCurrencyType, fromAccountName,toCurrencyType, toAccountName, amount):
        if(fromCurrencyType == "TL"): fromCurrency = "TRY"
        else: fromCurrency = fromCurrencyType

        if (toCurrencyType == "TL"): toCurrency = "TRY"
        else: toCurrency = toCurrencyType

        fromAccountId = self.AccountTable.getAccountIdFromAccountName(fromAccountName,userId)
        fromBalance = float(self.AccountTable.getAccountBalanceFromAccountName(fromAccountName, userId))

        toAccountId = self.AccountTable.getAccountIdFromAccountName(toAccountName,userId)
        toBalance = float(self.AccountTable.getAccountBalanceFromAccountName(toAccountName, userId))

        data = self.getCurrencyData(fromCurrency)
        self.AccountTable.updateBalance(float(fromBalance - amount), fromAccountId)
        self.AccountTable.updateBalance(float(toBalance + amount*float(data[toCurrency])), toAccountId)


    def getCorrespondingAmount(self, fromCurrencyType, toCurrencyType):
        data = self.getCurrencyData(fromCurrencyType)
        return data[toCurrencyType]






a = Account()

