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
        self.customer = customer
        self.acc=AC.Account()

    def getView(self, page):
        pass

    def openPage(self):
        view=CreateAccount.createWindow()
        while True:
            events, values = view.read()
            acc_name=values['accountName']
            acc_currency=values['currency']
            if(events=="Go Back" or events == sg.WIN_CLOSED):
                break
            elif(events=="CREATE ACCOUNT"):
                temp = self.acc.createAccount(acc_name,acc_currency,self.customer)
                if(acc_name == '' or acc_currency == ''):
                    sg.popup('Failed', 'Please fill all information!')
                    continue
                elif(temp == False):
                    sg.popup('Failed', 'You have an account with the same name!')
                    continue
                elif (temp == True):
                    sg.popup('Success', 'You Have Successfully created new Account')
                    break
        view.close()

