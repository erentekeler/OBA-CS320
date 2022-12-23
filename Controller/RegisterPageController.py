import sys
import os
import PySimpleGUI as sg
os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.insert(1,os.getcwd())
from GUI import registerPage
import Controller
from Controller import BankingController as bc
from Model import Customer as cus
#from Model import Account as acc

class RegisterPageController(bc.BankingController):
    def __init__(self) -> None:
        super().__init__()
        #self.model=self.getActionModel(registerPage)
        self.view=self.getView(registerPage)
    
    def getActionModel(self):
        pass
    def getView(self, registerPage):
        return registerPage.window
    
    def openPage(self):
        while True:
            events, values = self.view.read()
            name = values['Name']
            surname = values['Surname']
            tckn = values['ID']
            password = values['Password']
            if events == "Create Account":
                data=cus.Customer()
                if(data.registerCheck(tckn)):
                    data.createUser(name, surname, password, tckn)
                    sg.popup('Success', 'You have created your account successfully')
                    break
                elif(name == "" or surname == "" or tckn == "" or password == ""):
                    sg.popup('Missing Info','Please fill out everything!')
                elif(data.registerCheck(tckn)==False):
                    sg.popup('Existing ID','This ID already registered. Please Try to login!')
            elif events == "SIGN IN":
                break


        self.view.close()

