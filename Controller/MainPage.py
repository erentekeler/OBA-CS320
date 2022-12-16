import BankingController
import NewAccountPage
#import BankingModel
#import Customer
#import Account
#import Transaction

class MainPage(BankingController):
    
    def getActionModel():
        pass
    def getView():
        pass
    def __init__(self) -> None:
        super().__init__()
        self.model=self.getActionModel()
        self.view=self.getView()

    def clickCreateNewAccount(self):
        self.model.NewAccountPage()

    def clickListAccount(self):
        accounts = self.model.getAccounts()
        self.view.listAccounts(accounts)
    
    def clickLogout(self):
        self.model.logOut()
    
    def clickTransactionHistory(self):
        transactions = self.model.getTransactions()
        self.view.listTransactions(transactions)
    
    def clickBuySellCurrency(self):
        self.model.buySellCurrencyPage()
    
    def clickTransferMoney(self):
        self.model.TransferMoneyPage()

