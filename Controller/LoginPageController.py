import sys
import os
import py
os.path.normpath(os.getcwd() + os.sep + os.pardir)
sys.path.insert(1,os.getcwd())
from GUI import loginPage
import Controller
from Controller import BankingController as bc


class LoginPageController(bc.BankingController):
    def __init__(self) -> None:
        super().__init__()
        #self.model=self.getActionModel()
        #self.view=self.getView()
        self.window=self.getView(loginPage)
        

    def openPage(self):
        while True:
            events, values = self.window.read()   

            user_id = values['ID']
            user_password = values['Password']

            if(events == 'LOGIN'):
                #MainPage()
                break
            elif(events == 'REGISTER'):    
                #registerpage()
                break
        self.window.close()

    def getActionModel(self):
        pass
    def getView(self,loginPage):
        return loginPage.window



