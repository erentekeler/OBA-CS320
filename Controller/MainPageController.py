import sys
import os
os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.insert(1,os.getcwd())
from GUI import mainPage
import Controller
from Controller import BankingController as bc
#import NewAccountPage
#import BankingModel
#import Customer
#import Account
#import Transaction

class MainPageController(bc.BankingController):
    
    def getActionModel(self):
        pass
    def getView(self,mainPage):
        return mainPage.window
    
    def __init__(self,customer):
        super().__init__()
        self.customer=customer
        #self.model=self.getActionModel()
        self.view=self.getView(mainPage)

    #def clickCreateNewAccount(self):
     #   self.model.NewAccountPage()

    #def clickListAccount(self):
      #  accounts = self.model.getAccounts()
       # self.view.listAccounts(accounts)
    
    #def clickLogout(self):
    #    self.model.logOut()
    
    #def clickTransactionHistory(self):
     #   transactions = self.model.getTransactions()
      #  self.view.listTransactions(transactions)
    
    #def clickBuySellCurrency(self):
     #   self.model.buySellCurrencyPage()
    
    #def clickTransferMoney(self):
     #   self.model.TransferMoneyPage()

    def openPage(self):
        while True:
            events, values = self.view.read()
            if(events=="Create New Account"):
                break
            elif(events=="Logout"):
                break              
        self.view.close() 

