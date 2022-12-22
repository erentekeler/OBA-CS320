import sys
import os
os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.insert(1,os.getcwd())
from GUI import loginPage
import Controller
from Controller import MainPageController as mp
from Controller import BankingController as bc
from Controller import RegisterPageController as rg


class LoginPageController(bc.BankingController):
    def __init__(self) -> None:
        super().__init__()
        #self.model=self.getActionModel()
        #self.view=self.getView()
        self.view=self.getView(loginPage)
        

    def openPage(self):
        while True:
            events, values = self.view.read()   

            user_id = values['ID']
            user_password = values['Password']

            if(events == 'LOGIN'):
                #model
                self.view.close()
                main=mp.MainPageController()
                main.openPage()
                break
            elif(events == 'REGISTER'):    
                register=rg.RegisterPageController()
                register.openPage()
                continue
                
        self.view.close()
        

    def getActionModel(self):
        pass
    def getView(self,loginPage):
        return loginPage.window



a=LoginPageController()
a.openPage()