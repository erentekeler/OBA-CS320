import sys
import os
import PySimpleGUI as sg
os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.insert(1,os.getcwd())
from GUI import loginPage
import Controller
from Controller import MainPageController as mp
from Controller import BankingController as bc
from Controller import RegisterPageController as rg
from Model import Customer as cus
from Data import UserRepository as ur


class LoginPageController(bc.BankingController):
    def __init__(self) -> None:
        super().__init__()
        self.model=self.getActionModel(cus)
        self.view=self.getView(loginPage)
        

    def openPage(self):
        while True:
            events, values = self.view.read()   

            identitiy_num = values['ID']
            user_password = values['Password']

            if(events == 'LOGIN'):
                if(self.model.loginCheck(identitiy_num,user_password)):
                    self.view.close()
                    data=ur.UserRepository()
                    main=mp.MainPageController(data.getUserIdFromIdentityNo(identitiy_num))
                    main.openPage()
                    break
                elif(identitiy_num == "" or user_password==""):
                    sg.popup('Missing Info','Please fill your information first.')
                else:
                    sg.popup('Wrong Info','Wrong Id or Password! try again.')
                continue
            elif(events == 'REGISTER'):    
                register=rg.RegisterPageController()
                register.openPage()
                continue
                
        self.view.close()
        

    def getActionModel(self,model):
        return cus.Customer()
    def getView(self,loginPage):
        return loginPage.window



a=LoginPageController()
a.openPage()