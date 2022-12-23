import sys
import os
import PySimpleGUI as sg 
os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.insert(1, os.getcwd())
from GUI import CreateAccount
from Model import Account as AC


class NewAccountPageController():
    def __init__(self,customer) -> None:
        super().__init__()
        # self.model=self.getActionModel()
        # self.view=self.getView()
        self.view = self.getView(CreateAccount)
        self.customer = customer
        self.acc=AC.Account()

    def getView(self, page):
        return page.window

    def openPage(self):
        while True:
            events, values = self.view.read()
            acc_name=values['accountName']
            acc_currency=values['currency']
            if(events=="Go Back"):
                break
            elif(events=="CREATE ACCOUNT"):
                print(self.customer)
                if(acc_name == '' or acc_currency == '' or self.acc.createAccount(acc_name,acc_currency,self.customer)==False):
                    sg.popup('Failed', 'You need new account!')
                    continue
                elif (self.acc.createAccount(acc_name, acc_currency, self.customer)):
                    sg.popup('Success', 'You Have Successfully created new Account')
                    break

        self.view.close()

