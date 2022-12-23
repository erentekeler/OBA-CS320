import sys
import os
os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.insert(1, os.getcwd())
from Data import AccountRepository as ac
from GUI import transferMoneyPage
import PySimpleGUI as sg


class TransferMoneyPageController():
    def __init__(self) -> None:
        super().__init__()
        # self.model=self.getActionModel()
        # self.view=self.getView()
        self.view = self.getView(transferMoneyPage)
        self.ab = ac.AccountRepository()
        # self.userId = userId




    def getView(self, page):
        return page.window

    def openPage(self):

        while True:
            events, values = self.view.read()
            if(events =="Refresh Accounts List"):
                self.view['AccNames'].update(value='', values= self.ab.getAccountNamesOfUser(4))
            if(events == "AccNames"):
                self.view['Balance'].update('Account Balance:  '+str(self.ab.getAccountBalanceFromAccountName(values['AccNames'],4)[0]))
        self.view.close()


Tf = TransferMoneyPageController()
Tf.openPage()
