import sys
import os
import PySimpleGUI as sg
os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.insert(1, os.getcwd())
from GUI import registerPage
import Controller
from Controller import BankingController as bc
from Model import Customer as cus


# from Model import Account as acc

class RegisterPageController(bc.BankingController):
    def __init__(self) -> None:
        super().__init__()
        # self.model=self.getActionModel(registerPage)
        

    def getActionModel(self):
        pass

    def getView(self, registerPage):
        pass

    def openPage(self):
       
        view=registerPage.createWindow()
       
        while True:
            events, values = view.read()

            if events == "Create Account":
                data = cus.Customer()
                name = values['Name'].strip()
                surname = values['Surname'].strip()
                tckn = values['ID'].strip()
                password = values['Password']
                temp = data.registerCheck(tckn)
                if temp == True:
                    data.createUser(name, surname, password, tckn)
                    sg.popup('Success', 'You have created your account successfully')
                    break
                elif name == "" or surname == "" or tckn == "" or password == "":
                    sg.popup('Missing Info', 'Please fill out everything!')
                elif temp == str(8):
                    sg.popup('Existing ID', 'This ID already registered. Please Try to login!')
                elif temp == str(7):
                    sg.popup('Wrong ID type', 'ID should be 11 digits')
            elif events == "SIGN IN" or events == sg.WIN_CLOSED:
                name = ""
                surname = ""
                tckn = ""
                break

        view.close()
