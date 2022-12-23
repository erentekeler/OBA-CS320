import sys
import os
import PySimpleGUI as sg
os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.insert(1, os.getcwd())
from Data import AccountRepository as ac
from Model import Account as Acc
from Model import Transaction as TR
from GUI import transferMoneyPage
import PySimpleGUI as sg


class TransferMoneyPageController():
    def __init__(self, customer) -> None:
        super().__init__()
        # self.model=self.getActionModel()
        # self.view=self.getView()
        self.view = self.getView(transferMoneyPage)
        self.ab = ac.AccountRepository()
        self.acc=Acc.Account()
        self.transaction=TR.Transaction()
        self.customer=customer
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
            if(events==['Verify']):
                if(self.acc.findUser(values['recieverID'])):
                    self.view['reciever'].update('Receiver\'s Name : '+str(self.acc.findUser(values['recieverID'])))
                elif(self.acc.findUser(values['recieverID'])==False):
                    sg.popup('Fail','There is no matching account ID')
            if(events=='TRANSFER'):
                if(self.acc.findUser(values['recieverID'])==False):
                    sg.popup('Transfer Failed','There is no matching account ID')
                elif(float(values['amount'])<=self.ab.getAccountBalanceFromAccountName(values['AccNames'],4)[0]):
                    self.transaction.makeTransaction(self.customer,values['recieverID'],values['amount'])
                elif(float(values['amount']>self.ab.getAccountBalanceFromAccountName(values['AccNames'],4)[0])):
                    sg.popup('Transfer Fail', 'You don\'t have enough money')
            if(events=='Go Back'):
                break
        self.view.close()


Tf = TransferMoneyPageController()
Tf.openPage()
