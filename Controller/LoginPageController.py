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
        
        

    def openPage(self):
        view=loginPage.createWindow()
        while True:
            events, values = view.read()   

            if(events == 'LOGIN'):
                identitiy_num = values['ID']
                user_password = values['Password']
                if(self.model.loginCheck(identitiy_num,user_password)):
                    view.close()
                    data=ur.UserRepository()
                    print(data.getUserIdFromIdentityNo(identitiy_num))
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
                identitiy_num = ""
                user_password = ""
                continue
                
        view.close()
        

    def getActionModel(self,model):
        return cus.Customer()
    def getView(self,loginPage):
        pass



a=LoginPageController()
a.openPage()