import sys
import os
import PySimpleGUI as sg
os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.insert(1, os.getcwd())
from GUI import SellBuyCurrency
from Data import AccountRepository
from Model import Account


class BuySellCurrencyPageController():
    def __init__(self,customer) -> None:
        super().__init__()
        self.customer=customer
        self.ab= AccountRepository.AccountRepository()
        self.ac=Account.Account()
    def getView(self, page):
        pass

    def openPage(self):
        view = SellBuyCurrency.createWindow()
        while True:
            events, values = view.read()
            
            if(events=='fromAccName'):
                view['balance'].update('Balance:  '+str(self.ab.getAccountBalanceFromAccountName(values['fromAccName'],self.customer)[0]))
                continue
            elif(events=='fromCurType'):
                if(self.ab.getAccountNameFromCurrencyType(self.customer,values['fromCurType']) is not None):
                    view['fromAccName'].update(value='', values=self.ab.getAccountNameFromCurrencyType(self.customer,values['fromCurType']))
                if(values['toCurType']!=''):
                    view['currencyRate'].update('1 '+str(values['fromCurType'])+' = '+str(self.ac.getCorrespondingAmount(values['fromCurType'],values['toCurType']))+ ' ' +str(values['toCurType']))
            elif(events=='toAccName'):
                view['balanceTo'].update('Balance:  '+str(self.ab.getAccountBalanceFromAccountName(values['toAccName'],self.customer)[0]))
            elif(events=='toCurType'):
                if (self.ab.getAccountNameFromCurrencyType(self.customer, values['toCurType']) is not None):
                    view['toAccName'].update(value='', values=self.ab.getAccountNameFromCurrencyType(self.customer,values['toCurType']))
                if (values['fromCurType'] != ''):
                    view['currencyRate'].update('1 ' + str(values['fromCurType']) + ' = ' + str(self.ac.getCorrespondingAmount(str(values['fromCurType']),str(values['toCurType']))) + ' ' + str(values['toCurType']))
            elif(events=='amount'):
                if(values['fromCurType'] !='' and values['toCurType']!='' and values['amount'] != ''):
                    view['conver'].update(value=str(float(self.ac.getCorrespondingAmount(str(values['fromCurType']),str(values['toCurType'])))*float(values['amount']))+' '+str(values['toCurType']))
            elif(events=='Exchange'):
                if(values['amount']=='' or values['toAccName']=='' or values['fromAccName']==''):
                    sg.popup('Fail','Please fill up all informations')
                    continue
                elif(float(values['amount'])>self.ab.getAccountBalanceFromAccountName(values['fromAccName'],self.customer)[0]):
                    sg.popup('Fail','You don\'t have enough balance!')
                elif(values['fromCurType']==values['toCurType']):
                    sg.popup('Fail','You can\'t exchange money between same currency')
                elif(float(values['amount'])<=self.ab.getAccountBalanceFromAccountName(values['fromAccName'],self.customer)[0]):
                    self.ac.exchangeCurrency(self.customer,values['fromCurType'],values['fromAccName'],values['toCurType'],values['toAccName'],values['amount'])
                    sg.popup('Success','You have successfully exchange currency')
                break

            elif(events=='Go Back' or events== sg.WIN_CLOSED):
                break
        view.close()

