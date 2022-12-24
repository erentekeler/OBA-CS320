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
        self.ab = ac.AccountRepository()
        self.acc=Acc.Account()
        self.transaction=TR.Transaction()
        self.customer=customer
        # self.userId = userId




    def getView(self, page):
        pass

    def openPage(self):
        view=transferMoneyPage.createWindow()
        while True:
            
            events, values = view.read()

            if(events =="Refresh Accounts List"):
                view['AccNames'].update(value='', values= self.ab.getAccountNamesOfUser(self.customer))
            elif(events == "AccNames"):
                view['Balance'].update('Account Balance:  '+str(self.ab.getAccountBalanceFromAccountName(values['AccNames'],self.customer)[0]))
            elif(events == 'Verify'):
                if(self.acc.getUserFullNameFromAccountId(values['receiverID'])):
                    view['reciever'].update('Receiver\'s Name : '+str(self.acc.getUserFullNameFromAccountId(values['receiverID'])))
                elif(self.acc.getUserFullNameFromAccountId(values['receiverID'])==False):
                    view['reciever'].update('Receiver\'s Name : ' + str("Not Found!"))
                    sg.popup('Fail','There is no matching account ID')
            elif(events=='TRANSFER'):
                temp = values['AccNames']
                if(self.acc.getUserFullNameFromAccountId(values['receiverID'])==False):
                    sg.popup('Transfer Failed','There is no matching account ID')
                elif(float(values['amount'])<=self.ab.getAccountBalanceFromAccountName(values['AccNames'],self.customer)[0] and self.transaction.makeTransaction(values["AccNames"],self.customer,values['receiverID'],values['amount'])):
                    sg.popup('Transfer Succsessful','Your new balance is ' + str(self.ab.getAccountBalanceFromAccountName(temp,self.customer)[0] - float(values['amount'])) + ' Thank you for choosing OBA')
                    break
                elif(self.transaction.makeTransaction(values["AccNames"],self.customer,values['receiverID'],values['amount']) == False):
                    print("imdat")
                    sg.popup('Transfer Failed', 'Currency type should match!')
                elif(float(values['amount'])>self.ab.getAccountBalanceFromAccountName(values['AccNames'],self.customer)[0]):
                    sg.popup('Transfer Fail', 'You don\'t have enough money')

            elif(events=='Go Back' or events == sg.WIN_CLOSED):
                break

        view.close()



