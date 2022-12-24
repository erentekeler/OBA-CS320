import sys
import os
os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.insert(1, os.getcwd())
from GUI import AccountList
from Data import AccountRepository
from Data import AccountRepository as ac

class AccountsPageController():
    def __init__(self,customer) -> None:
        super().__init__()
        # self.model=self.getActionModel()
        # self.view=self.getView()
        self.customer=customer
        self.ab=ac.AccountRepository()

    def getView(self, loginPage):
        pass

    def openPage(self):
        view=AccountList.createWindow()
        while True:
            events, values =view.read()
            if(events=='Go Back'):
                break
            elif(events=='Refresh Accounts'):
                view['AccNames'].update(value='', values= self.ab.getAccountNamesOfUser(self.customer))
            elif(events=='AccNames'):
                view['Balance'].update('Balance:  '+str(self.ab.getAccountBalanceFromAccountName(values['AccNames'],self.customer)[0]))
                view['currency'].update('Currency Type: '+str(self.ab.getCurrencyFromAccountName(values['AccNames'],self.customer)[0]))
                view['accID'].update('Account ID: '+str(self.ab.getAccountIdFromAccountName(values['AccNames'],self.customer[0])))
        view.close()



