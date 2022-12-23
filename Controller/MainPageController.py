import sys
import os
os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.insert(1,os.getcwd())
from GUI import mainPage
import Controller
from Controller import BankingController as bc
from Controller import NewAccountPageController as Na
from Controller import AccountsPageController as ap
from Controller import TransferMoneyPageController as Tf
from Controller import TransactionHistoryController as Th
from Controller import BuySellCurrencyPageController as Bs


class MainPageController(bc.BankingController):
    
    def getActionModel(self):
        pass
    def getView(self,mainPage):
        return mainPage.window
    
    def __init__(self,customer):
        super().__init__()
        self.customer=customer
        self.view=self.getView(mainPage)


    def openPage(self):
        while True:
            events, values = self.view.read()
            if(events=="Create New Account"):
                newaccountpage=Na.NewAccountPageController(self.customer)
                newaccountpage.openPage()
            elif(events=='List Accounts'):
                listaccpage=ap.AccountsPageController(self.customer)
                listaccpage.openPage()
            elif(events=='Transfer Money'):
                transfer=Tf.TransferMoneyPageController(self.customer)
                transfer.openPage()
            elif(events=='Transaction History'):
                transaction=Th.TransactionHistoryController(self.customer)
                transaction.openPage()
            elif(events=='Buy/Sell Currency'):
                buysell=Bs.BuySellCurrencyPageController(self.customer)
                buysell.openPage()
            elif(events=="Logout"):
                break              
        self.view.close() 

