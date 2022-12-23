import sys
import os
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
            tckn = values['givenID']
            password = values['Password']
            if events == "Create Account":
                customer = cus.Customer()
                if customer.registerCheck(tckn):
                    customer.createUser(name, surname, password, tckn)
            elif events == "SIGN IN":
                break


        self.view.close()

